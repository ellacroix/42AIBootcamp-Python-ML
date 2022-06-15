import sys
from CsvReader import CsvReader
import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    def fit(self, data):
        cluster = []
        for n in range(0, kc.ncentroid):
            cluster.append([])
        for p in data:
            d = []
            for i in range(0, self.ncentroid):
                d.append(np.linalg.norm(p[1:] - self.centroids[i, 1:]))		# L2distance
            closest_centroid = d.index(min(d))
            cluster[closest_centroid].append(p.tolist())
        for i in range(0, self.ncentroid):
            self.centroids[i][1:] = np.average(cluster[i], axis=0)[1:]


    def predict(self, data):
        arr = []
        for p in data:
            d = []
            for i in range(0, self.ncentroid):
                d.append(np.linalg.norm(p[1:] - self.centroids[i, 1:]))		# L2distance
            closest_centroid = d.index(min(d))
            arr.append(closest_centroid)
        return arr


if __name__ == "__main__":
    kc = KmeansClustering()
    with CsvReader("../ressources/solar_system_census.csv") as file:
        data = np.array(file.getdata())
    data = data[1:].astype(float)
    maxh = np.amax(data[0:, 1])
    minh = np.amin(data[0:, 1])
    maxw = np.amax(data[0:, 2])
    minw = np.amin(data[0:, 2])
    maxb = np.amax(data[0:, 3])
    minb = np.amin(data[0:, 3])
    for i in range(0, kc.ncentroid):
        kc.centroids.append([i, random.uniform(minh, maxh), random.uniform(minw, maxw), random.uniform(minb, maxb)])
    kc.centroids = np.array(kc.centroids)
    # print(kc.centroids)
    # print(kc.centroids[0,1:])
    # L1distance = sum(np.abs(kc.centroids[0,1:] - kc.centroids[1,1:]))
    # print(L1distance)
    # L2distance = np.linalg.norm(kc.centroids[0,1:] - kc.centroids[1,1:])
    # print(L2distance)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    c = kc.predict(data)
    ax.scatter(data[..., 1], data[..., 2], data[..., 3], c=c)
    ax.scatter(kc.centroids[0][1], kc.centroids[0][2], kc.centroids[0][3], s=100, c="purple")
    ax.scatter(kc.centroids[1][1], kc.centroids[1][2], kc.centroids[1][3], s=100, c="blue")
    ax.scatter(kc.centroids[2][1], kc.centroids[2][2], kc.centroids[2][3], s=100, c="green")
    ax.scatter(kc.centroids[3][1], kc.centroids[3][2], kc.centroids[3][3], s=100, c="yellow")
    ax.set_title('Initial situation')
    for i in range(1,30):
        kc.fit(data)
    c = kc.predict(data)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter(data[..., 1], data[..., 2], data[..., 3], c=c)
    ax.scatter(kc.centroids[0][1], kc.centroids[0][2], kc.centroids[0][3], s=100, c="purple")
    ax.scatter(kc.centroids[1][1], kc.centroids[1][2], kc.centroids[1][3], s=100, c="blue")
    ax.scatter(kc.centroids[2][1], kc.centroids[2][2], kc.centroids[2][3], s=100, c="green")
    ax.scatter(kc.centroids[3][1], kc.centroids[3][2], kc.centroids[3][3], s=100, c="yellow")
    ax.set_title('After K-means')
    plt.show()

