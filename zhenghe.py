import pyaudio
import wave
from aip import AipSpeech
import datetime
import time
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
def wwav():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "D:\\test.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,channels = CHANNELS,rate = RATE,input = True,frames_per_buffer = CHUNK)

    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def shibie():
    APP_ID = '17673156'
    API_KEY = 'VuOEZqEHiQmv6brzxjWpvVqq'
    SECRET_KEY = 'So5k1Topwq7frkeGo7jzr5jOeVrvcnak'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    file_handle = open('D:\\test.wav', 'rb')
    file_content = file_handle.read()

    result = client.asr(file_content, 'pcm', 16000, {
        'dev_pid': '1536',
    })

    if result['err_no'] == 0:
        #print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " >> " + result['result'][0])
         print(result['result'][0])
    else:
        print(str(result['err_no']))
        #print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " >> " + "err_no:" + str(result['err_no']))
if __name__=='__main__':
    wwav()
    time.sleep(1)
    shibie()
    time.sleep(2)