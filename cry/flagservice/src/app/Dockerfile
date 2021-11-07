FROM python:3.9-alpine

RUN apk add \
  build-base \
  gcc \
  gmp-dev \
  linux-headers \
  musl-dev

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]
