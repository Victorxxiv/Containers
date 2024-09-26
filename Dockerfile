# Base image from the official Python image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory content into the container
COPY . /app

# Install the required Python packages
RUN pip install flask

# Expose the port the app will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]