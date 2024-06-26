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
    postgresql-dev \
    gcc \
    musl-dev \
    && rm -rf /var/cache/apk/* \
    && pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Expose port 8000 to the outside world
EXPOSE 8000

# Set environment variables for GDAL
ENV GDAL_DATA=/usr/share/gdal
ENV PROJ_LIB=/usr/share/proj
ENV GEOS_LIBRARY_PATH=/usr/lib/libgeos_c.so

RUN python restaurants_project/manage.py collectstatic --noinput
# Run migrations and start the server
CMD ["sh", "-c", "python restaurants_project/manage.py migrate && python restaurants_project/manage.py runserver 0.0.0.0:8000"]
