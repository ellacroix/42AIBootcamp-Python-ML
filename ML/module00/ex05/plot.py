import numpy as np
import matplotlib.pyplot as plt

def predict_(x, theta):
	"""Computes the vector of prediction y_hat from two non-empty numpy.array.
	Args:
	x: has to be an numpy.array, a vector of shape m * 1.
	theta: has to be an numpy.array, a vector of shape 2 * 1.
	Returns:
	y_hat as a numpy.array, a vector of shape m * 1.
	None if x or theta are empty numpy.array.
	None if x or theta shapes are not appropriate.
	None if x or theta is not of the expected type.
	Raises:
	This function should not raise any Exception.
	"""
	X = np.hstack((np.ones((x.shape[0],1)), x))
	return (np.dot(X, theta))

def simple_predict(x, theta):
	return np.array(theta[0] + x * theta[1]).astype(float)

def plot(x, y, theta):
	"""Plot the data and prediction line from three non-empty numpy.array.
	Args:
	x: has to be an numpy.array, a vector of shape m * 1.
	y: has to be an numpy.array, a vector of shape m * 1.
	theta: has to be an numpy.array, a vector of shape 2 * 1.
	Returns:
	Nothing.
	Raises:
	This function should not raise any Exception.
	"""
	plt.plot(predict_(x, theta))
	#plt.plot(simple_predict(x,theta))
	plt.plot(y, 'ro')
	plt.show()

x = np.arange(1,6).reshape((5,1))
y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
# Example 1:
theta1 = np.array([4.5, -0.2])
plot(x, y, theta1)
# Example 2:
theta2 = np.array([-1.5, 2])
plot(x, y, theta2)
# Example 3:
theta3 = np.array([3, 0.3])
plot(x, y, theta3)