# Use a lighter base image
FROM python:3.8-slim AS base

# Set the working directory in the container
WORKDIR /app

# Copy both the source code and the requirements file into the container
COPY . /app
COPY requirements.txt /app/requirements.txt

# Install dependencies and set a longer timeout
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Set the entrypoint
CMD ["python", "app.py"]
