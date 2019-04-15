import pyaudio
import wave
import glob

# 録音時間
RECORD_SECOND = 5

# 録音デバイスの番号
iDeviceIndex = 0

get_file_index = glob.glob("audio[0-9]*.wav")
get_file_index.sort(reverse = True)

if len(get_file_index) != 0:
    max_index = ''.join(c for c in get_file_index[0] if c.isdigit())
    this_index = int(max_index) + 1

else:
    this_index = 1

# 録音情報の設定
FORMAT = pyaudio.paInt16 #音声のフォーマット
CHANNELS = 2             
RATE = 44100             #サンプルレート
CHUNK = 1024            
audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS,
        rate=RATE, input=True,
        input_device_index = iDeviceIndex, #録音デバイスのインデックス番号
        frames_per_buffer=CHUNK)
 
all = []
for i in range(0, int(RATE / CHUNK * RECORD_SECOND)):
    data = stream.read(CHUNK)
    all.append(data)

print("finished recording")

stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open("audio"+ str(this_index) + ".wav", 'w')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(all))
waveFile.close()