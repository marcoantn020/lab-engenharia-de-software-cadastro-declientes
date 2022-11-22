FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /var/www/app/

WORKDIR /var/www/app/

EXPOSE 80 5000