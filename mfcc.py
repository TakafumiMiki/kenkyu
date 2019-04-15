import librosa, librosa.display
import numpy as np
import matplotlib.pyplot as plt
import glob

def visualize(sig, fs):
    data = []
    melspecs = librosa.feature.melspectrogram(y=sig, sr=fs,
                                            n_fft=2048, n_mels=128)
    data.extend(melspecs)
    """
    librosa.display.specshow(librosa.power_to_db(melspecs, ref=np.max),
                            x_axis='time', y_axis='mel', fmax=fs)

    plt.colorbar(format='%+2.0f dB')
    plt.show()
    """
    return data
get_file_index = glob.glob("audio[0-9]*.wav")

for i in get_file_index:
    sig, fs = librosa.audio.load(i)
    data = visualize(sig, fs)
    # dataは1つあたり128次元 (上のn_melsで決定) 
    print(len(data))

# svmしやすい形で保存したい
# with open("ashioto.txt", mode='w') as f:
#     f.writelines(data)
