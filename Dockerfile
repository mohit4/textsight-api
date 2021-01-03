FROM python:3.8-alpine

MAINTAINER Mohit Kumar [ https://github.com/mohit4 ]

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt requirements.txt

RUN pip install -r /requirements.txt
RUN mkdir /app
WORKDIR /app

RUN adduser -D myAppUser
USER myAppUser