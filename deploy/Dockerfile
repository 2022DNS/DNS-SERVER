FROM python:slim

RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev

# build-essential includes default libraries.: ILoveGameCoding
RUN apt-get install -y build-essential

ENV PYTHONBUFFERED 1
RUN pip install django
RUN pip install djangorestframework
RUN pip install pymysql
RUN pip install mysqlclient

# This package used for Facial Landmark Detection.: ILoveGameCoding
RUN pip install cmake
RUN pip install opencv-python
RUN pip install dlib

COPY . code/
WORKDIR code/

RUN python manage.py migrate

ENTRYPOINT python manage.py runserver 0.0.0.0:80

EXPOSE 80