import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


y = np.loadtxt("y_label.csv", delimiter=",", dtype=int)
X = np.loadtxt("X_data.csv", delimiter=",")
# X = preprocessing.minmax_scale(X[:, 1:]) 
X_train, X_test, y_train, y_test = train_test_split(X, y.ravel(), test_size=0.3)

clf = SVC(kernel="rbf", C=1)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(y_pred)
acs = accuracy_score(y_test, y_pred)
print(acs)