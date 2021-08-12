FROM python:3.8-slim-buster 

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN apt-get update -y
RUN apt-get install -y libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 
RUN apt-get install -y ffmpeg
RUN apt-get install -y python-pyaudio
RUN apt purge timidity-daemon

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]