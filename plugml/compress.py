from sklearn.decomposition import TruncatedSVD

class Compressor(object):
    def __init__(self, extractor, dim):
        self.extractor = extractor
        self.dim = dim
        self._svd = TruncatedSVD(dim)
        self._svd.fit(self.extractor.get())

    def get(self):
        return self._svd.transform(self.extractor.get())

    def transform(self, data):
        return self._svd.transform(data)