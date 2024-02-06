# Use an official Python runtime as a parent image
FROM python:3.11.4-slim-buster

# Create and set the working directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip
COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod a+x /usr/src/app/docker-entrypoint.sh
ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]
