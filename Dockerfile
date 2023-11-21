# base image  
FROM python:3.8   

ARG DB_ENGINE
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT

ENV DB_ENGINE=$DB_ENGINE
ENV DB_NAME=$DB_NAME
ENV DB_USER=$DB_USER
ENV DB_PASSWORD=$DB_PASSWORD
ENV DB_HOST=$DB_HOST
ENV DB_PORT=$DB_PORT

# setup environment variable  
ENV DockerHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

COPY ./requirements.txt  ./requirements.txt

# run this command to install all dependencies  
RUN python3 -m  pip install -r requirements.txt  

# copy whole project to your docker home directory. 
COPY . $DockerHOME  

# port where the Django app runs  
EXPOSE 8000

# start server  
RUN python3 manage.py makemigrations
# RUN python3 manage.py migrate
CMD python3 manage.py runserver 
