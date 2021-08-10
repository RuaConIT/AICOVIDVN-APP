from re import S
from survey import models
from django.http import HttpResponse
from django.shortcuts import render
import sounddevice
from scipy.io.wavfile import write
from src.dataclass import AudioData
from src.preprocess import normalize_audio
from src.utils import load_audio_data
import librosa
import joblib
import numpy as np
from survey.forms import SurveyForm
from survey.models import Survey
import uuid
import os
from multiprocessing import Queue
import multiprocessing


def home(request):
    if request.method == 'POST':
        audio_file = record(request)

        def create(request, q):
            survey = SurveyForm(request.POST)
            if survey.is_valid():
                obj = survey.save(commit=False)
                filename = str(uuid.uuid4())
                write('record/%s.wav' % filename, 44100, audio_file)
                obj.uuid = filename
                obj.audio_path = filename + '.wav'
                obj.save()
                q.put(filename)

        q = Queue()
        pool = multiprocessing.Process(target=create, args=[request, q])
        pool.start()
        pool.join()
        return render(request, 'record.html', {'uuid_id': q.get()})

    else:
        survey = SurveyForm()
        return render(request, 'home.html', {'form': survey})


def calculator(data: AudioData, **librosa_mfcc_kwargs) -> AudioData:
    result = []
    sr = data.sampling_rate
    y = data.features.wav
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    spec_cent = librosa.feature.spectral_centroid(y=y,
                                                  sr=sr,
                                                  **librosa_mfcc_kwargs)
    #rmse = librosa.feature.rmse(y=y)
    spec_bw = librosa.feature.spectral_bandwidth(y=y,
                                                 sr=sr,
                                                 **librosa_mfcc_kwargs)
    rolloff = librosa.feature.spectral_rolloff(y=y,
                                               sr=sr,
                                               **librosa_mfcc_kwargs)
    zcr = librosa.feature.zero_crossing_rate(y, **librosa_mfcc_kwargs)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, **librosa_mfcc_kwargs)
    to_append = f'{np.mean(chroma_stft)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
    for i in mfcc:
        to_append += f' {np.mean(i)}'
    data.features.allfeat = np.array(str(to_append).split(' ')).astype(
        np.float)
    return data


def result(request, uuid_id):
    s = Survey.objects.get(uuid=uuid_id)
    form = SurveyForm(instance=s)
    obj = form.save(commit=False)
    audio = load_audio_data('record', uuid_id)
    audio = normalize_audio(audio)
    audio_extraction = calculator(audio)
    model = joblib.load('model/knn_model.pkl', mmap_mode='r')
    y_predict = model.predict(
        (audio_extraction.features.allfeat).reshape(1, -1))
    if y_predict == 1:
        obj.result = True
        obj.save()
        return render(request, 'result.html', {"y_predict": y_predict})
    else:
        obj.result = False
        obj.save()
        return render(request, 'result.html', {"y_predict": y_predict})


def record(request):
    audio_cough = sounddevice.rec(int(7 * 44100), samplerate=44100, channels=2)
    sounddevice.wait()
    return audio_cough
