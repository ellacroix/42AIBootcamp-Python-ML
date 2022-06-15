import numpy as np

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
	X = np.c_[np.ones((len(x), 1)), x]
	return (np.dot(X, theta))

x = np.arange(1,6).reshape((5,1))
#x = np.arange(6,1)
# Example 1:
theta1 = np.array([5, 0])
print(predict_(x, theta1))
# Example 2:
theta2 = np.array([0, 1])
print(predict_(x, theta2))
# Example 3:
theta3 = np.array([5, 3])
print(predict_(x, theta3))
# Example 4:
theta4 = np.array([-3, 1])
print(predict_(x, theta4))