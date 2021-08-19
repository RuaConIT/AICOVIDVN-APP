FROM python:3.8
ENV PYTHONUNBUFFERED=1
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
RUN . /opt/venv/bin/activate && pip install --upgrade pip
RUN . /opt/venv/bin/activate && pip install -r requirements.txt
RUN . /opt/venv/bin/activate && pip install pyaudio
CMD . /opt/venv/bin/activate
  
