# Pull base image
FROM python:3.6-alpine

# Set work directory
WORKDIR /code

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /code/Pipfile
RUN pipenv install --deploy --system --skip-lock --dev

# Copy project
COPY . /code/