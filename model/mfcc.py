import glob
import librosa
import librosa.display
import numpy as np
# import matplotlib.pyplot as plt
# import csv
# ラベル数が増えた場合にline 34 のy_labelを変更する必要あり

def visualize(sig, fs):
    # n_mel は出力するデータ量
    melspecs = librosa.feature.melspectrogram(y=sig, sr=fs,
                                              n_fft=2048, n_mels=256)

    # Vlibrosa.display.specshow(librosa.power_to_db(melspecs, ref=np.max),
    #                        x_axis='time', y_axis='mel', fmax=fs)

    # plt.colorbar(format='%+2.0f dB')
    # plt.show()

    return melspecs

def craete_ylabel():
    # files_name = glob.glob(path + "*.wav")
    # files_num = len(files_name)
    # print(files_num)
    X_num = []
    for name in y_list:
        X_num.append(len(glob.glob(path + name + "*.wav")))

    # y labelの作成
    return X_num

path = "..\\splitsound_files\\"
y_list = ["ashioto", "kaze", "typing"]
get_file = glob.glob(path + "*.wav")
split_file_names = craete_ylabel()

y_data = []
for i in range(len(split_file_names)):
    y_data += [i for _ in range(split_file_names[i])]
# print(y_data)
# print(len(y_data))

X_data = []
for j in range(sum(split_file_names)):
    signal, sample = librosa.audio.load(get_file[j])
    data = visualize(signal, sample)
    X_data.append(data.ravel())

    if j == 0:
        print(len(data), data.ndim)
    elif j == 1:
        print(len(data), data.ndim)
        
else:
    print(len(data), len(data.ravel()))
    print(X_data[-1], len(X_data))

y_data = np.array(y_data)
X_data = np.array(X_data)
np.savetxt("y_label.csv", y_data, delimiter=",")
np.savetxt("X_data.csv", X_data, delimiter=",")

"""
# 追加書き込みじゃない
# for X_data_fin in X_data:
#     np.savetxt("X_data.csv", X_data_fin, delimiter=",")
# csvじゃなくnpのほうがいい
# with open("model.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(y_data)
#     for name in X_data:
#         print(len(name))
#         writer.writerows(name)
#     print(len(X_data))
"""