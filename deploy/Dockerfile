FROM python:slim

RUN sudo apt-get install libssl-dev
RUN pip install django
RUN pip install pymysql
RUN pip install mysqlclient

COPY . code/
WORKDIR code/

RUN python manage.py migrate

ENTRYPOINT python manage.py runserver 0.0.0.0:80

EXPOSE 80