FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev
RUN apk del .tmp-build-deps

RUN mkdir /barbershop
WORKDIR /barbershop
COPY ./barbershop /barbershop

# COPY ./barbershop/requirements.txt /requirements.txt
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2-binary
RUN pip install -r /barbershop/requirements.txt

#
# RUN mkdir /barbershop
# WORKDIR /barbershop
# COPY ./barbershop /barbershop

RUN adduser -D user
USER user