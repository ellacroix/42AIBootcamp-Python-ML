import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from data_spliter import data_spliter
from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR

def zscore(x):
	m = len(x)
	mean = (sum(x) / m)
	var = sum((x - mean) ** 2) / m
	x_prime = (x - mean) / (var ** (1 / 2))
	return x_prime

data = pd.read_csv("../ressources/space_avocado.csv")
X = np.array(data[['weight', 'prod_distance', 'time_delivery']]).reshape(-1,3)
continuous_X = np.concatenate((np.arange(0, 100, 1).reshape(-1,1), np.arange(1000, 3000, 20).reshape(-1,1), np.arange(0, 20, 0.2).reshape(-1,1)), axis = 1).reshape(-1,3)
Y = np.array(data[['target']]).reshape(-1,1)

Xsplit, Ysplit = data_spliter(X, Y, 0.8)
#Xsplit[0]: x_train Xsplit[1]: x_test

#Multivariate Linear Model
"""theta = np.array([40000, 4000, 100, 100]).reshape(-1,1)
mylr = MyLR(theta, 1e-7, 10000)


y_hat = mylr.predict_(Xsplit[0])
print("MSE base:\t{}".format(mylr.mse_(Ysplit[0], y_hat)))
plt.plot(data['weight'], Y, 'o')					#scatter whole dataset
y_hat = mylr.predict_(continuous_X)
plt.plot(continuous_X[:,0], y_hat)
plt.show()
mylr.fit_(Xsplit[0], Ysplit[0])
y_hat = mylr.predict_(Xsplit[0])
print("MSE train:\t{}".format(mylr.mse_(Ysplit[0], y_hat)))
plt.plot(Xsplit[0][:,0], Ysplit[0], 'o')			#scatter train dataset
y_hat = mylr.predict_(continuous_X)
plt.plot(continuous_X[:,0], y_hat)
plt.show()
y_hat = mylr.predict_(Xsplit[1])
print("MSE test:\t{}".format(mylr.mse_(Ysplit[1], y_hat)))
plt.plot(Xsplit[1][:,0], Ysplit[1], 'o')			#scatter test dataset
y_hat = mylr.predict_(continuous_X)
plt.plot(continuous_X[:,0], y_hat)
plt.show()
print(mylr.thetas)"""

#Multivariate Polynomial Model, COMMENT FAIRE ?
theta = np.array([40000, 4000, 400, 100, 100]).reshape(-1,1)
mylr = MyLR(theta, 4e-7, 10000)


#plt.plot(data['weight'], Y, 'o')
#plt.plot(data['prod_distance'], Y, 'o')
#plt.plot(data['time_delivery'], Y, 'o')
#plt.show()