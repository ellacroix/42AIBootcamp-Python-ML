import numpy as np
import random as rd
from sklearn.linear_model import LogisticRegression as LR

class MyLogisticRegression():
    """
    Description:
    My personnal logistic regression to classify things.
    """
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
    
    def data_spliter(self, x, y, proportion):
        x_train = []
        x_test = []
        y_train = []
        y_test = []
        index = [i for i in range(len(x))]
        rd.shuffle(index)
        prop = proportion * len(x)
        i = 0
        while i < prop:
            x_train.append(x[index[i]])
            y_train.append(y[index[i]])
            i += 1
        while i < len(x):
            x_test.append(x[index[i]])
            y_test.append(y[index[i]])
            i += 1
        return (np.array(x_train), np.array(x_test), np.array(y_train), np.array(y_test))

if __name__ == '__main__':
    X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [3., 5., 9., 14.]])
    Y = np.array([[1], [0], [1]]).reshape(-1,1)
    theta = np.array([2, 0.5, 7.1, -4.3, 2.09]).reshape(-1,1)
    mylr = MyLogisticRegression(theta)
    # Example 0:
    print(mylr.predict_(X))
    # Example 1:
    print(mylr.loss_(X,Y))
    # Example 2:
    mylr.fit_(X, Y)
    print(mylr.theta)
    # Example 3:
    print(mylr.predict_(X))
    # Example 4:
    print(mylr.loss_(X,Y))