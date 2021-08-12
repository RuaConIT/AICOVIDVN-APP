FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN mkdir .app
WORKDIR /app

COPY requirements.txt /app/
RUN apt-get update -y

RUN apt-get install -y portaudio19-dev python-all-dev python3-all-dev && pip3 install pyaudio

RUN pip3 install -r requirements.txt
RUN apt-get install -y libsndfile1

COPY . /app/
