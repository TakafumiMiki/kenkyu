import glob

import librosa
import librosa.display
# import numpy as np
# import matplotlib.pyplot as plt


def visualize(sig, fs):
    melspecs = librosa.feature.melspectrogram(y=sig, sr=fs,
                                              n_fft=2048, n_mels=100)

    # Vlibrosa.display.specshow(librosa.power_to_db(melspecs, ref=np.max),
    #                        x_axis='time', y_axis='mel', fmax=fs)

    # plt.colorbar(format='%+2.0f dB')
    # plt.show()

    return melspecs


get_file_index = glob.glob("..\\audio_file\\audio[0-9]*.wav")
TEST_DATA_NUM = len(get_file_index) // 2
TRAIN_DATA_NUM = len(get_file_index) - TEST_DATA_NUM
# print(TRAIN_DATA_NUM)
# print(TEST_DATA_NUM)

try:
    if TRAIN_DATA_NUM > 3 or TEST_DATA_NUM > 3:
        tra_data = []
        pred_data = []

        for i in range(TRAIN_DATA_NUM):
            signal, sample = librosa.audio.load(get_file_index[i])
            tra_data.append(visualize(signal, sample))
            # data = np.append(data, visualize(sig, fs))

        for j in range(TRAIN_DATA_NUM, len(get_file_index)):
            signal, sample = librosa.audio.load(get_file_index[-j])
            pred_data.append(visualize(signal, sample))

        # print(len(data), len(pred_data))
        # if data[-1] is pred_data[0]:
        #     print("missing")

        # else:
        #     print("ok")

    else:
        raise ValueError

except ValueError:
    print("データ数が足りません")
