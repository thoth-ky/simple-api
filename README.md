# Simple API Deployment to GKE
This project demonstrates how to deploy a simple python project (in this case a FAST API project) to GKE using Cloud Build and using Ansible to Provision a GKE cluster.

Cloud build is configured with a trigger to auto deploy the project when a commit is pushed to the `main` branch.

# Provisoon GKE CLuster

Provision a cluster, specified as `prod-cluster`

## Reguirements
- Ansible
- [GCP Ansible Collection](https://galaxy.ansible.com/google/cloud?extIdCarryOver=true&sc_cid=701f2000001OH7YAAW)

## Prerequisites
1. Obtain a GCP default Compute Engine service account file(usually `.json`) and place it at the root folder of the project
2. Obtain the Google Project ID

## Steps

1. Ensure all the requirents are isntalled in the virtual environment
    ```
    $ pip install -r requirements.txt"
    ```
2. Run the playbook with the following option to provide for the google project id
    ```
    $ ansible-playbook -e project_name=<GCP_PROJECT_ID> ansible/playbook.yml
    ```

# Run FASTAPI

## Local Setup Steps

1. Ensure all requirements are in the local environemt
    ```
    $ pip install -r requirements.txt"
    ```
2. Run the API in dev mode
    ```
    $ uvicorn main:app --reload
    ```
3. Navigate to `http://127.0.0.1:8000/docs` to read the API docs
4. A simple TODO list can be found in `http://127.0.0.1:8000/fe`



# Authors
- Joseph M Kyalo