import sounddevice
import multiprocessing

def record():
    audio_cough = sounddevice.rec(int(7 * 44100), samplerate=44100, channels=2)
    sounddevice.wait()
    return audio_cough

p = multiprocessing.Process(target=record)
p.start()