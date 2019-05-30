import input_audio
import librosa, librosa.display
import numpy as np
import matplotlib.pyplot as plt

before_data = input_audio.data
data = np.frombuffer(before_data, dtype="int16") / 32768.0

fs = input_audio.fs


melspecs = librosa.feature.melspectrogram(y=data, sr=fs,
                                          n_fft=2048, n_mels=128)

librosa.display.specshow(librosa.power_to_db(melspecs, ref=np.max),
                         x_axis='time', y_axis='mel', fmax=fs)

plt.colorbar(format='%+2.0f dB')
plt.show()