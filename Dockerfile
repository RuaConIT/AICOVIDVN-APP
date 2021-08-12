FROM python:3.8-slim-buster 

RUN mkdir .app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

# RUN apt-get update -y
# RUN apt-get install -y libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 
# RUN apt-get install -y ffmpeg
# RUN apt-get install -y python-pyaudio
# RUN apt purge timidity-daemon

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]