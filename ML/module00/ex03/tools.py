import numpy as np

def add_intercept(x):
	"""Adds a column of 1’s to the non-empty numpy.array x.
	Args:
	x: has to be an numpy.array, a vector of shape m * 1.
	Returns:
	x as a numpy.array, a vector of shape m * 2.
	None if x is not a numpy.array.
	None if x is a empty numpy.array.
	Raises:
	This function should not raise any Exception.
	"""
	return np.hstack((np.ones((x.shape[0],1)), x))

x = np.arange(1,6).reshape((5,1))
print(add_intercept(x))
# Example 2:
y = np.arange(1,10).reshape((3,3))
print(add_intercept(y))