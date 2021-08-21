FROM python:3.8
RUN mkdir .app
WORKDIR /app

COPY requirements.txt /app/
# 

# RUN pip3 install -r requirements.txt

# RUN apt-get install -y portaudio19-dev python-all-dev python3-all-dev && pip3 install pyaudio

COPY . /app/



RUN apt-get update -y
RUN apt-get install -y portaudio19-dev python-all-dev python3-all-dev
RUN apt-get install -y libsndfile1


RUN python3 -m venv /opt/venv
ENV PATH /opt/venv/bin/activate:$PATH
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install pyaudio

