# Use the official Python image as base
FROM python:3.12-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies, including GDAL
RUN apk add --update --no-cache \
    gdal \
    gdal-dev \
    geos \
    geos-dev \
    proj \
    proj-dev \
    && rm -rf /var/cache/apk/* \
    && pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Expose port 8000 to the outside world
EXPOSE 8000

# Start the application
CMD ["python", "restaurants_project/manage.py", "runserver", "0.0.0.0:8000"]
