FROM python:slim

RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
RUN apt-get -y install libgl1-mesa-glx
# build-essential includes default libraries.: ILoveGameCoding
RUN apt-get install -y build-essential

COPY . code/
WORKDIR code/

ENV PYTHONBUFFERED 1
RUN pip install cmake

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN python manage.py migrate

ENTRYPOINT python manage.py runserver 0.0.0.0:80

EXPOSE 80