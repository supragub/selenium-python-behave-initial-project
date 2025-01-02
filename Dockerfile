# Use the official Python image from the Docker Hub
FROM python:3.12.6-bullseye

# Set the working directory in the container
WORKDIR /app

# Setting environment variable
ENV RUNNING_IN_DOCKER=true

# Creating log directory
RUN mkdir -p /app/logs

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Chromium WebDriver for Selenium
RUN apt-get update && apt-get install -y chromium-driver

# Install Allure CLI
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk-headless wget unzip && \
    wget https://github.com/allure-framework/allure2/releases/download/2.13.8/allure-2.13.8.zip && \
    unzip allure-2.13.8.zip -d /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure

# Copy the rest of the application code into the container
COPY . /app
