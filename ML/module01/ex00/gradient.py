import numpy as np

def simple_gradient(x, y, theta):
	"""Computes a gradient vector from three non-empty numpy.array, without any for-loop.
	The three arrays must have compatible shapes.
	Args:
	x: has to be an numpy.array, a vector of shape m * 1.
	y: has to be an numpy.array, a vector of shape m * 1.
	theta: has to be an numpy.array, a 2 * 1 vector.
	Return:
	The gradient as a numpy.array, a vector of shape 2 * 1.
	None if x, y, or theta are empty numpy.array.
	None if x, y and theta do not have compatible shapes.
	None if x, y or theta is not of the expected type.
	Raises:
	This function should not raise any Exception.
	"""
	X = np.c_[np.ones((len(x), 1)), x]
	y_hat = np.dot(X, theta)
	#print("{} . {} = {}".format(X, theta, y_hat))
	partial_derivative0 = sum(y_hat - y)/len(x)
	partial_derivative1 = sum((y_hat - y)*x)/len(x)
	return(np.array([partial_derivative0, partial_derivative1]))


x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])
# Example 0:
theta1 = np.array([2, 0.7])
print(simple_gradient(x, y, theta1))
# Output:
#array([-19.0342574 -586.66875564])
# Example 1:
theta2 = np.array([1, -0.4])
print(simple_gradient(x, y, theta2))
#array([-57.86823748 -2230.12297889])