import numpy as np
from scipy.sparse import hstack
from sklearn.preprocessing import StandardScaler

class Extractor:
    def __init__(self, features):
        self.feats = features
        self.names = [feat.name for feat in self.feats]
        self._map = {name:i for name, i in zip(self.names, range(len(self.feats)))}
        self.featNames = [feat.featNames for feat in self.feats]
        self.featNames = [name for names in self.featNames for name in names]

    def __getitem__(self, key):
        # Return column.
        if isinstance(key, basestring):
            return self.feats[self._map[key]][:]
        # Return row.
        if isinstance(key, (int, long, np.int64)):
            return hstack([feat[key] for feat in self.feats])
        # Return element.
        row, col = key
        if isinstance(col, basestring):
            e = self.feats[self._map[col]][row]
        else:
            e = self.feats[col][row]
        return e

    def get(self):
        return hstack([feat.data for feat in self.feats])

    def transform(self, data):
        if isinstance(data, list):
            return [self.transform(elem) for elem in data]
        checked = {name:0 for name in self.names}
        for key in data:
            checked[key] = 1
        for key in checked:
            if checked[key] == 0:
                data[key] = None
        feats = hstack([feat.transform([data[feat.name]]) for feat in self.feats])
        return feats


