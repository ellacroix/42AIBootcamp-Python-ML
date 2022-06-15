import numpy as np
import matplotlib.pyplot as plt
from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
from sklearn.preprocessing import minmax_scale

def zscore(x):
	m = len(x)
	mean = (sum(x) / m)
	var = sum((x - mean) ** 2) / m
	x_prime = (x - mean) / (var ** (1 / 2))
	return x_prime

x = np.arange(1,11).reshape(-1,1)
y = np.array([[ 1.39270298],
[ 3.88237651],
[ 4.37726357],
[ 4.63389049],
[ 7.79814439],
[ 6.41717461],
[ 8.63429886],
[ 8.19939795],
[10.37567392],
[10.68238222]])

# Build the model:
x_ = add_polynomial_features(x, 3)
#x_ = minmax_scale(x_)
x_ = zscore(x_)
my_lr = MyLR(np.ones(4).reshape(-1,1), alpha=1e-1, max_iter=200000)
my_lr.fit_(x_, y)
y_hat = my_lr.predict_(x_)
# Plot:
## To get a smooth curve, we need a lot of data points
continuous_x = np.arange(1,10.01, 0.01).reshape(-1,1)
x_ = add_polynomial_features(continuous_x, 3)
x_ = zscore(x_)
#print(x_.shape)
#print(my_lr.thetas.shape)
y_hat = my_lr.predict_(x_)
plt.scatter(x,y)
plt.plot(continuous_x, y_hat, color='orange')
plt.show()