#################################################################
# Dockerfile for the Eno-Configuration Service
# Based on Python 3.6.2
#################################################################

FROM python:3.6.2

MAINTAINER FlaskApp Learning Sessions "ryan.conrad@maxwellhealth.com"

# Install Dependencies
ADD requirements.txt /usr/Flask/requirements.txt
Run pip install -r /usr/Flask/requirements.txt

# Add the application
ADD . /usr/Flask

# Set the default directory for the application
WORKDIR /usr/Flask

# Set the environment variable name
ENV NAME Garuda

# Expose port for database
EXPOSE 3500
