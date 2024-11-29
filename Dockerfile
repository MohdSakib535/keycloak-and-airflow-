# # Dockerfile

# FROM apache/airflow:2.7.0

# USER airflow

# # Copy requirements.txt into the image
# COPY requirements.txt /requirements.txt

# # Install Python dependencies
# RUN pip install --no-cache-dir -r /requirements.txt





# Use the official Apache Airflow image as the base
FROM apache/airflow:2.6.3

# Switch to root to install dependencies
USER root

# Install necessary packages for OIDC
RUN pip install apache-airflow-providers-google apache-airflow-providers-redis apache-airflow-providers-postgres flask_oidc

# Switch back to airflow user
USER airflow

# Set environment variables if needed
ENV AIRFLOW_HOME=/opt/airflow
