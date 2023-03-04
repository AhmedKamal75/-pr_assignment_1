import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA


def pca(dataset,a=alphanums,built_in=True,normalize=True):
    if normalize:
        normalized_data = MinMaxScaler().fit_transform(dataset)
    if built_in:
         print(alpha)
         pca = PCA(n_components=alpha)
         X_pca = pca.fit_transform(normalized_data)
    else:
        data_mean = 
    return X_pca



if __name__ == "__main__":
    pass