FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt update
RUN yes | apt install vi

COPY ./ /app
WORKDIR /app

ENV STATIC_URL /app/static
ENV STATIC_PATH /var/www/app/static

RUN apt install gunicorn
RUN pip install -r /app/requirements.txt
RUN gunicorn -c config.py main:app
RUN service nginx start