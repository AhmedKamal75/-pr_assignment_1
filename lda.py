import numpy as np

def calcMeans(x, n = 5, m = 40):
    means = [] # array of vectors each represent the means
    #print(m * n + 1)
    temp = []

    for i in range (m * n + 1):
        temp += x[i]
        if (i != 0) and (i % n == 0):
            temp /= n
            means.append(temp)
            temp = []


    return np.array(means);






def lda(x, y, n = 5, m = 40, built_in=True, normalize=False):
    #get the mean of each class
    means = calcMeans(x, n, m)

    # over all mean
    mean = []
    for i in range (m + 1):
        mean += means[i]
    mean /= m

    #sb
    sb = []
    for i in range(m + 1):
        temp = (mean[i] - mean)
        sb += n * temp * np.transpose(temp)

    #to be continued

if __name__ == "__main__":
    pass