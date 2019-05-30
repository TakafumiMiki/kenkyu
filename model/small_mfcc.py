import glob
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


def visualize(sig, fs):
    # n_mel は出力するデータ量
    melspecs = librosa.feature.melspectrogram(y=sig, sr=fs,
                                              n_fft=2048, n_mels=100)

    librosa.display.specshow(librosa.power_to_db(melspecs, ref=np.max),
                           x_axis='time', y_axis='mel', fmax=fs)

    plt.colorbar(format='%+2.0f dB')
    plt.show()

    return melspecs

path = "..\\splitsound_files\\"
sound_name = "shisaku" + ".wav"

