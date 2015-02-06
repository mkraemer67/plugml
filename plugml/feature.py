import numpy as np
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Imputer, StandardScaler

class RawFeature(object):
    def __init__(self, data, col):
        self.name = col
        self._scaler = None
        self._imputer = None
        self._vec = None
        self.data = self._preprocess(data[col])
        self._setup()
        self.data = self.transform(self.data, False)

    def _preprocess(self, data):
        return np.matrix(data, dtype=np.double).T

    def _setup(self):
        self.featNames = [self.name + "##raw"]
        self.dim = 1

    def transform(self, data, preprocess=True):
        if data[0] != None:
            feats = self._preprocess(data) if preprocess else data
            if self._vec:
                feats = self._vec.transform(feats)
        else:
            feats = [np.nan for i in range(self.dim)]
        if not self._imputer:
            self._imputer = Imputer()
            self._imputer.fit(feats)
        feats = self._imputer.transform(feats)
        if not self._scaler:
            # Sparse matrices cannot be normalized regarding mean.
            # This detection should not be done with try/except though.
            try:
                self._scaler = StandardScaler()
                self._scaler.fit(feats)
            except:
                self._scaler = StandardScaler(with_mean=False)
                self._scaler.fit(feats)
        feats = self._scaler.transform(feats)
        return feats

    def __getitem__(self, key):
        return self.data[key]

class CategoricalFeature(RawFeature):
    def _preprocess(self, data):
        prefix = self.name + "##cat##"
        return [{prefix+cat.lower():1 for cat in arr} for arr in data]

    def _setup(self):
        self._vec = DictVectorizer()
        self._vec.fit(self.data)
        self.featNames = self._vec.get_feature_names()
        self.dim = len(self.featNames)

class TextFeature(RawFeature):
    def __init__(self, data, col):
        self._tokenizer = RegexpTokenizer(r"\w\w+")
        self._stemmer = LancasterStemmer()
        self._stopwords = stopwords.words("english")
        self._prefix = col + "##txt##"
        super(TextFeature, self).__init__(data, col)

    def _preprocess(self, data):
        return [self._tokenizeText(text) for text in data]

    def _setup(self):
        self._vec = TfidfVectorizer(
            analyzer=lambda x: x,
            sublinear_tf=True,
            smooth_idf=True,
            norm='l2',
            min_df=2,
            max_df=0.9
        )
        self._vec.fit(self.data)
        self.featNames = self._vec.get_feature_names()
        self.dim = len(self.featNames)

    def _tokenizeText(self, text):
        tokens = [t.lower() for t in self._tokenizer.tokenize(text.decode('utf-8'))]
        tokens = [self._prefix + self._stemmer.stem(t) for t in tokens
            if t not in self._stopwords]
        return tokens