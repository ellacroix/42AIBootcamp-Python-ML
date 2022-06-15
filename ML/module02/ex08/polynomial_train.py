import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR

def zscore(x):
	m = len(x)
	mean = (sum(x) / m)
	var = sum((x - mean) ** 2) / m
	x_prime = (x - mean) / (var ** (1 / 2))
	return x_prime

theta1 = np.array([1, -10]).reshape(-1,1)
theta2 = np.array([1, -10, 1]).reshape(-1,1)
theta3 = np.array([1, -10, 1, 1]).reshape(-1,1)
theta4 = np.array([1, 160, -80, 10, -1]).reshape(-1,1)
theta5 = np.array([1, -1850, 1110, -305, 40, -2]).reshape(-1,1)
#theta6 = np.array([9110, -18015, 13400, -4935, 966, -96.4, 3.86]).reshape(-1,1)
theta6 = np.array([1, 18, 64, -93, -372, 206, 434]).reshape(-1,1)

data = pd.read_csv("../ressources/are_blue_pills_magics.csv")
data = np.array(data[['Micrograms', 'Score']])
data = zscore(data)
print(data)
#X = np.array(data[['Micrograms']])
#Y = np.array(data[['Score']])
X = np.array(data[:, 0].reshape(-1,1))
Y = np.array(data[:, 1].reshape(-1,1))
continuous_X = np.arange(-2, 1.51, 0.01).reshape(-1,1)
fig, ax = plt.subplots()
plt.xlabel("x: Micrograms")
plt.ylabel("y: Score")
plt.scatter(X,Y)


my_plr1 = MyLR(theta1, alpha = 1e-1, max_iter=10000)
my_plr1.fit_(X, Y)
y_hat1 = my_plr1.predict_(X)
print("MSE my_plr1 = {}".format(my_plr1.mse_(Y, y_hat1)))
print("thetas my_plr1 = {}".format(my_plr1.thetas))
plt.plot(X, y_hat1, color='blue', label='pl1')

X2 = add_polynomial_features(X, 2)
my_plr2 = MyLR(theta2, alpha = 1e-1, max_iter=10000)
my_plr2.fit_(X2, Y)
y_hat2 = my_plr2.predict_(X2)
print("MSE my_plr2 = {}".format(my_plr2.mse_(Y, y_hat2)))
print("thetas my_plr2 = {}".format(my_plr2.thetas))
X2 = add_polynomial_features(continuous_X, 2)
X2 = zscore(X2)
y_hat2 = my_plr2.predict_(X2)
plt.plot(continuous_X, y_hat2, color='purple', label='pl2')

X3 = add_polynomial_features(X, 3)
X3 = zscore(X3)
my_plr3 = MyLR(theta3, alpha = 1e-1, max_iter=10000)
my_plr3.fit_(X3, Y)
y_hat3 = my_plr3.predict_(X3)
print("MSE my_plr3 = {}".format(my_plr3.mse_(Y, y_hat3)))
print("thetas my_plr3 = {}".format(my_plr3.thetas))
X3 = add_polynomial_features(continuous_X, 3)
X3 = zscore(X3)
y_hat3 = my_plr3.predict_(X3)
plt.plot(continuous_X, y_hat3, color='pink', label='pl3')

X4 = add_polynomial_features(X, 4)
X4 = zscore(X4)
my_plr4 = MyLR(theta4, alpha = 1e-1, max_iter=10000)
my_plr4.fit_(X4, Y)
y_hat4 = my_plr4.predict_(X4)
print("MSE my_plr4 = {}".format(my_plr4.mse_(Y, y_hat4)))
print("thetas my_plr4 = {}".format(my_plr4.thetas))
X4 = add_polynomial_features(continuous_X, 4)
X4 = zscore(X4)
y_hat4 = my_plr4.predict_(X4)
plt.plot(continuous_X, y_hat4, color='red', label='pl4')

"""X5 = add_polynomial_features(X, 5)
X5 = zscore(X5)
my_plr5 = MyLR(theta5, alpha = 4e-1, max_iter=100000)
my_plr5.fit_(X5, Y)
y_hat5 = my_plr5.predict_(X5)
print("MSE my_plr5 = {}".format(my_plr5.mse_(Y, y_hat5)))
print("thetas my_plr15 = {}".format(my_plr5.thetas))
X5 = add_polynomial_features(continuous_X, 5)
X5 = zscore(X5)
y_hat5 = my_plr5.predict_(X5)
plt.plot(continuous_X, y_hat5, color='green', label='pl5')"""

"""X6 = add_polynomial_features(X, 6)
X6 = zscore(X6)
my_plr6 = MyLR(theta6, alpha = 3e-1, max_iter=500000)
my_plr6.fit_(X6, Y)
y_hat6 = my_plr6.predict_(X6)
print("MSE my_plr6 = {}".format(my_plr6.mse_(Y, y_hat6)))
print("thetas my_plr6 = {}".format(my_plr6.thetas))
X6 = add_polynomial_features(continuous_X, 6)
X6 = zscore(X6)
y_hat6 = my_plr6.predict_(X6)
plt.plot(continuous_X, y_hat6, color='orange', label='pl6')
"""

ax.legend()
plt.show()