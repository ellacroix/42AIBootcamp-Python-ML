import numpy as np

def loss_(y, y_hat):
	"""Computes the mean squared error of two non-empty numpy.array, without any for loop.
	The two arrays must have the same shapes.
	Args:
	y: has to be an numpy.array, a vector.
	y_hat: has to be an numpy.array, a vector.
	Return:
	The mean squared error of the two vectors as a float.
	None if y or y_hat are empty numpy.array.
	None if y and y_hat does not share the same shapes.
	None if y or y_hat is not of expected type.
	Raises:
	This function should not raise any Exception.
	"""
	return np.dot((y_hat - y),(y_hat-y))/(2*len(y))

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
""" X = np.array([	[23.],
			 	[48.], 
			 	[218.]])
Y = np.array([	[20.],
			 	[48.], 
			 	[1.]]) """
# Example 0:
print(loss_(X, Y))
# Example 1:
print(loss_(X, X))