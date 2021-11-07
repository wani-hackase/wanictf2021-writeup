FROM python:3.9-alpine

RUN apk --no-cache add socat

RUN apk add gcc
RUN apk add musl-dev
RUN apk add gmp-dev

RUN pip install pycryptodome

ADD chall.py chall.py
ADD secret.py secret.py

CMD socat -dd -v >/dev/stdout TCP-L:50000,fork,reuseaddr EXEC:"python -u chall.py"
