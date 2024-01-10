<<<<<<< HEAD
# Use an official Python runtime as a parent image
FROM python:3.8-slim
=======
FROM python:3.12
>>>>>>> c759d162d6e99bdc3fcca769ec3df2b4b88daf38

WORKDIR /app

<<<<<<< HEAD
# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "ThePantryPuzzle\main.py"]
=======
COPY . /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc libffi-dev

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["python", "main.py"]
>>>>>>> c759d162d6e99bdc3fcca769ec3df2b4b88daf38
