FROM python:3.9.1-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app


RUN useradd apiuser && chown -R apiuser /app
USER apiuser

EXPOSE 8000
CMD ["uvicorn", "main:app"]
