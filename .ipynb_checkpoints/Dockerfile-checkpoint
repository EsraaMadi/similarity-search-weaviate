FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN pip install --upgrade "protobuf<=3.20.1"

COPY . .
