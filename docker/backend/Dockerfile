FROM --platform=linux/amd64 python:3.10.6-alpine

RUN apk update && apk add python3-dev gcc libc-dev

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn==20.1.0

ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./picasso /app/picasso
ADD ./docker /app/docker

RUN chmod +x /app/docker/backend/server-entrypoint.sh
RUN chmod +x /app/docker/backend/worker-entrypoint.sh