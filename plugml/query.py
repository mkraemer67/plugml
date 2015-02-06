import numpy as np
from sklearn.neighbors import NearestNeighbors

class KNN(object):
    def __init__(self, data):
        self._nn = NearestNeighbors(algorithm='brute', metric='cosine')
        self._nn.fit(data)

    def query(self, v, k=10):
        _,idx = self._nn.kneighbors(v, k)
        return idx[0]