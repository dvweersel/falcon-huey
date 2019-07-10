import time
import numpy as np
import json
import jsonpickle
from sklearn.base import BaseEstimator, RegressorMixin


class Regressor(BaseEstimator, RegressorMixin):

    def __init__(self, degree):
        self.B = None
        self.d = degree

    @staticmethod
    def xtoX(self, x):
        X = np.empty((len(x), self.degree + 1))
        for i in range(self.degree + 1):
            X[:,i] = x**i
        return X

    def fit(self, x, y):
        X, Y = self.xtoX(x, self.d), y
        time.sleep(np.random.randint(10, 30))  # simulate slow computation
        self.B = np.linalg.pinv((X.T).dot(X)).dot((X.T).dot(Y))

    def predict(self, x):
        if self.B is None:
            raise Exception('Model not fitted!')

        time.sleep(np.random.randint(10, 30))  # simulate slow computation
        return self.xtoX(x, self.d).dot(self.B)

    def save(self, path='data/model.json'):
        with open(path, 'w') as f:
            json.dump(jsonpickle.encode(self), f)  # making sure the output is serializable

    def load(self, path='data/model.json'):
        with open(path, 'r') as f:
            m = f.read()
        return jsonpickle.decode(json.loads(m))

# def save(model, path='model.json'):
#     with open(path, 'w') as f:
#         json.dump(jsonpickle.encode(model), f)  # making sure the output is serializable
#
#
# def load(path='model.json'):
#     with open(path, 'r') as f:
#         m = f.read()
#     return jsonpickle.decode(json.loads(m))