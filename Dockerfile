# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=main.py

# Expose the port that the Flask app will listen on
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
