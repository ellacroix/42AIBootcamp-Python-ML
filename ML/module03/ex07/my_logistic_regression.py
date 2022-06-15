import numpy as np
import random as rd
from sklearn.linear_model import LogisticRegression as LR

class MyLogisticRegression():
    def __init__(self, theta, alpha=0.001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.theta = theta

    def predict_(self, x):
        y_hat = np.dot(np.c_[np.ones((len(x), 1)), x], self.theta)
        return 1 / (1 + np.exp(-y_hat)).reshape(-1,1)

    def gradient_(self, x, y, theta):
        m = len(x)
        X = np.c_[np.ones((len(x), 1)), x]
        y_hat = self.predict_(x)
        grad = (1 / m) * (np.dot(np.transpose(X), (y_hat - y)))
        return grad

    def fit_(self, x, y):
        m = len(x)
        X = np.c_[np.ones((len(x), 1)), x]
        y_hat = self.predict_(x)
        i = 0
        while i < self.max_iter:
            gradient = self.gradient_(x, y, self.theta)
            self.theta = self.theta - self.alpha * gradient
            i += 1
        return self.theta

    def loss_(self, x, y):
        eps = 1e-15
        y_hat = self.predict_(x)
        return sum(sum((y * np.log(y_hat + eps)) + ((1 - y) * np.log(1 - y_hat + eps))) / -len(y))
