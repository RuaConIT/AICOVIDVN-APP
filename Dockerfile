FROM python:3.8-slim-buster 

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# RUN python3 import os
# RUN os.system("sudo apt-get install --reinstall alsa-base pulseaudio")
# RUN os.system("sudo alsa force-reload")
# RUN pip3 install pulseaudio
# RUN apt-get install build-essential -y
# RUN apt-get install alsa-utils -y
# RUN alsa force-reload
#     apt-get -y install sudo
# RUN apt-get update && apt-get upgrade
# RUN apt-get install libasound2 alsa-utils alsa-oss -y
# RUN alsamixer

RUN apt-get update
RUN apt-get install -y pulseaudio socat
RUN apt-get install -y alsa-utils
RUN apt-get install -y ffmpeg
RUN pulseaudio -D --exit-idle-time=-1

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]