import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA


def pca(dataset, alpha=0.95, built_in=True, normalize=False):
    if normalize:
        dataset = MinMaxScaler().fit_transform(dataset)
    if built_in:
        pca = PCA(n_components=alpha)
        X_pca = pca.fit_transform(dataset)
    else:
        # mean for every feature
        mean_vector = np.array([np.mean(dataset[:, i]) for i in range(dataset.shape[1])])
        # centered data
        Z = dataset - mean_vector
        # covariance matrix S, it is symmetric matrix
        S = (np.matmul(Z.transpose(), Z)) / Z.shape[1]
        # get eigenvalues w, eigenvectors v ordered increasingly
        w, v = np.linalg.eigh(S)

    # return X_pca
    return "this is the return value"


if __name__ == "__main__":
    pass
