import numpy as np
from math import sqrt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def mse_(y, y_hat):
	return sum((y_hat - y) ** 2)/(len(y))

def rmse_(y, y_hat):
	return sqrt(mse_(y, y_hat))

def mae_(y, y_hat):
	return sum(abs(y_hat - y))/len(y)

def r2score_(y, y_hat):
	return 1 - (sum((y_hat - y)**2))/(sum((y - np.mean(y))**2))


y = np.array([0, 15, -9, 7, 12, 3, -21])
y_hat = np.array([2, 14, -13, 5, 12, 4, -19])
# Mean squared error
## your implementation
print(mse_(y,y_hat))
## sklearn implementation
print(mean_squared_error(y,y_hat))
# Root mean squared error
## your implementation
print(rmse_(y,y_hat))
## sklearn implementation not available: take the square root of MSE
print(sqrt(mean_squared_error(y,y_hat)))
# Mean absolute error
## your implementation
print(mae_(y,y_hat))
## sklearn implementation
print(mean_absolute_error(y,y_hat))
# R2-score
## your implementation
print(r2score_(y,y_hat))
## sklearn implementation
print(r2_score(y,y_hat))