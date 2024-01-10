# Use a Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app code into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port your Flask app runs on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to start the Flask app
CMD ["flask", "run"]
