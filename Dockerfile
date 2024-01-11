FROM python:3.12

WORKDIR /app

# Copy the Flask app code into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches

COPY . /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc libffi-dev

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["python", "main.py"]
