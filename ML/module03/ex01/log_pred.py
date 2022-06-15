import numpy as np

def logistic_predict_(x, theta):
	"""Computes the vector of prediction y_hat from two non-empty numpy.array.
	Args:
	x: has to be an numpy.array, a vector of shape m * n.
	theta: has to be an numpy.array, a vector of shape (n + 1) * 1.
	Return:
	y_hat: a numpy.array of shape m * 1, when x and theta numpy arrays
	with expected and compatible shapes.
	None: otherwise.
	Raises:
	This function should not raise any Exception.
	"""
	y_hat = np.dot(np.c_[np.ones((len(x), 1)), x], theta)
	return np.array(1 / (1 + np.exp(-y_hat)))

if __name__ == '__main__':
	# Example 1
	x = np.array([4])
	theta = np.array([[2], [0.5]])
	print(logistic_predict_(x, theta))
	# Example 1
	x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
	theta2 = np.array([[2], [0.5]])
	print(logistic_predict_(x2, theta2))
	# Example 2
	x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
	theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
	print(logistic_predict_(x3, theta3))