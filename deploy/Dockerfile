FROM python:slim

RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
ENV PYTHONBUFFERED 1
RUN pip install django
RUN pip install pymysql
RUN pip install mysqlclient

COPY . code/
WORKDIR code/

RUN python manage.py migrate

ENTRYPOINT python manage.py runserver 0.0.0.0:80

EXPOSE 80