from sklearn.svm import SVC
import numpy as np
import mfcc

# ラベル付け
X = np.array([mfcc.tra_data[i] for i in range(mfcc.TRAIN_DATA_NUM)])
X = X.reshape(X.shape[0], -1)
# yはラベル
y = np.array([0, 1, 2, 2, 0])

clf = SVC()
clf.fit(X, y)
# predictで次の音声データのラベルを予測する

for j in range(mfcc.TEST_DATA_NUM):
    pred_data = np.array([mfcc.pred_data[j]])
    pred_data = pred_data.reshape(pred_data.shape[0], -1)
    print(clf.predict(pred_data))
