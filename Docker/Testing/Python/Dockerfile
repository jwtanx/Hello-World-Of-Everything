# Specify which python you are using
FROM python:3.8

# COPY THE REQUIRED FILES INTO THE DOCKER
COPY requirements.txt .

# INTALLATION AND SETUP
RUN pip install -r requirements.txt


COPY . . 

EXPOSE 5000
