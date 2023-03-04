import numpy as np
import cv2
import os
from generate_data import reformat_dataset
from pca import pca
# from sklearn.model_selection import train_test_split



# counting from 0
def split_dataset_oscillate(X, y):
    X_train = []
    X_test = []
    y_train = []
    y_test = []
    for i in range(X.shape[0]):
        if (i%2) == 0: # even
            X_test.append(X[i])
            y_test.append(y[i])
        else:
            X_train.append(X[i])
            y_train.append(y[i])

    return np.array(X_train), np.array(X_test), np.array(y_train), np.array(y_test)



if __name__ == "__main__":
    X, y = reformat_dataset(path=os.path.join("archive"))
    # X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.5)
    X_train, X_test, y_train, y_test = split_dataset_oscillate(X,y)
    print(pca(X_train,built_in=False))
    print(pca(X_test,built_in=False))