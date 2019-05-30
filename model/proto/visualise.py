import numpy as np
import matplotlib.pyplot as plt
import input_audio

data = input_audio.data
x = np.frombuffer(data, dtype="int16") / 32768.0

plt.figure(figsize=(15,3))
plt.plot(x)
plt.show()

x = np.fft.fft(np.frombuffer(data, dtype="int16"))

plt.figure(figsize=(15,3))
plt.plot(x.real[:int(len(x)/2)])
plt.show()