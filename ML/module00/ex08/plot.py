import numpy as np
import matplotlib.pyplot as plt

def loss_(y, y_hat):
	if len(y) != len(y_hat):
		raise ValueError("Not same dimensions")
	result = (np.dot((y_hat - y), (y_hat - y)))/(2*len(y))
	return result
	
def plot_with_loss(x, y, theta):
	y_hat = np.dot(np.c_[np.ones((len(x), 1)), x], theta)
	cost = loss_(y, y_hat) * 2
	plt.plot(x, y, 'o')
	plt.plot(x, y_hat)
	i = 0
	while i < len(x):
		plt.plot([x[i], x[i]],[y[i], y_hat[i]] , 'r--')
		i += 1
	plt.title("Cost : {}".format(cost))
	plt.show()

x = np.arange(1,6)
y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])
# Example 1:
theta1= np.array([18,-1])
plot_with_loss(x, y, theta1)
# Example 2:
theta2 = np.array([14, 0])
plot_with_loss(x, y, theta2)
# Example 3:
theta3 = np.array([12, 0.8])
plot_with_loss(x, y, theta3)