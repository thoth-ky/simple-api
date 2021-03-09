#!/bin/bash

# Create a new node-pool
NEW_POOL_NAME=${NEW_POOL_NAME}
CLUSTER_NAME=${CLUSTER_NAME}
MACHINE_TYPE=${MACHINE_TYPE}
NUM_NODES=${NUM_NODES}
OLD_POOL_NAME=${OLD_POOL_NAME}

echo "NEW POOL NAME:" $NEW_POOL_NAME
echo "CLUSTER_NAME:" $CLUSTER_NAME
echo "MAchine Type:"$MACHINE_TYPE
echo "Num of Nodes:" $NUM_NODES
echo "Old Pool Name:" $OLD_POOL_NAME


gcloud container node-pools create $NEW_POOL_NAME --cluster=$CLUSTER_NAME --machine-type=${MACHINE_TYPE} --num-nodes=$((NUM_NODES))

# List availabe nodepools
gcloud container node-pools list --cluster=$CLUSTER_NAME

# Mark existing nodepool as unschedulable

for node in $(kubectl get nodes -l cloud.google.com/gke-nodepool=$OLD_POOL_NAME -o=name); do
    kubectl cordon "$node";
done


#  Drain existing nodepool

for node in $(kubectl get nodes -l cloud.google.com/gke-nodepool=$OLD_POOL_NAME -o=name); do
    kubectl drain --force --ignore-daemonsets --delete-local-data --grace-period=10 "$node";
done

gcloud container node-pools delete $OLD_POOL_NAME --cluster=$CLUSTER_NAME -q