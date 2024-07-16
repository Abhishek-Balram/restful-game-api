# Use an official Python runtime as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the API requirements file into the container
COPY api/requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the API code into the container
COPY api/app.py .
COPY api/.env .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--debug" ]
