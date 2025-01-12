# Dockerfile example
FROM python:3.8-slim

WORKDIR /app

# Copy the required files into the container
COPY . .

# Install the necessary dependencies
RUN pip install -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Command to run the app
CMD ["python", "app.py"]
