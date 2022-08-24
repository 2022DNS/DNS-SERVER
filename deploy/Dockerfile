FROM python:slim

RUN pip install django

COPY . code/
WORKDIR code/

RUN python manage.py migrate

ENTRYPOINT python manage.py runserver 0.0.0.0:80

EXPOSE 80