from my_logistic_regression import MyLogisticRegression as MyLR
from data_spliter import data_spliter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def zscore(x):
	m = len(x)
	mean = (sum(x) / m)
	var = sum((x - mean) ** 2) / m
	x_prime = (x - mean) / (var ** (1 / 2))
	return x_prime

zipcode = 2

dataX = pd.read_csv("../ressources/solar_system_census.csv")
dataY = pd.read_csv("../ressources/solar_system_census_planets.csv")
X = np.array(dataX[['height', 'weight', 'bone_density']]).reshape(-1,3)
X = zscore(X)
Y = np.array(dataY[['Origin']]).reshape(-1,1)
Y = (Y == zipcode).astype(float)

Xsplit, Ysplit = data_spliter(X, Y, 0.7)

theta = np.array([0,1,1,1]).reshape(-1,1)
mylr = MyLR(theta, 1e-1, 10000)

plt.scatter(X[:,0], Y)
plt.scatter(X[:,0], mylr.predict_(X))
plt.show()

mylr.fit_(Xsplit[0], Ysplit[0])
y_hat = mylr.predict_(Xsplit[1])
pred = (y_hat >= 0.5).astype(int)
print("Correct guesses: {}/{}".format(np.sum(pred == Ysplit[1]), len(Ysplit[1])))

plt.scatter(X[:,0], Y)
plt.scatter(X[:,0], mylr.predict_(X))
plt.show()

plt.scatter(X[:,1], Y)
plt.scatter(X[:,1], mylr.predict_(X))
plt.show()

plt.scatter(X[:,2], Y)
plt.scatter(X[:,2], mylr.predict_(X))
plt.show()