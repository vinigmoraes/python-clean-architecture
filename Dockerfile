# set base image (host OS)
FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app

RUN apt-get update
RUN mkdir /app

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt /app

# install dependencies
RUN pip install -r /app/requirements.txt

# copy the content of the local src directory to the working directory
COPY . /app

# command to run on container start
CMD [ "python", "/app/library/application/app.py" ]
