import numpy as np


def simple_predict(x, theta):
	"""Computes the prediction vector y_hat from two non-empty numpy.array.
	Args:
	x: has to be an numpy.array, a matrix of shape m * n.
	theta: has to be an numpy.array, a vector of shape (n + 1) * 1.
	Return:
	y_hat as a numpy.array, a vector of shape m * 1.
	None if x or theta are empty numpy.array.
	None if x or theta shapes are not appropriate.
	None if x or theta is not of expected type.
	Raises:
	This function should not raise any Exception.
	"""
	#print(x)
	#print(x.shape)
	y_hat = []
	for i in range(0, x.shape[0]):
		#print(x[i])
		yi = theta[0]
		for j in range(0, x.shape[1]):
			#print("{} * {}".format(x[i][j], theta[j+1]))
			yi += x[i][j] * theta[j+1]
		#print(yi)
		y_hat.append(yi)
	#print(y_hat)
	return(y_hat)



x = np.arange(1,13).reshape((4,-1))
# Example 0:
theta1 = np.array([5, 0, 0, 0])
simple_predict(x, theta1)
# Ouput:
#array([5., 5., 5., 5.])
# Do you understand why y_hat contains only 5’s here?
# Example 1:
theta2 = np.array([0, 1, 0, 0])
simple_predict(x, theta2)
# Output:
#array([ 1., 4., 7., 10.])
# Do you understand why y_hat == x[:,0] here?
# Example 2:
theta3 = np.array([-1.5, 0.6, 2.3, 1.98])
simple_predict(x, theta3)
# Output:
#array([ 9.64, 24.28, 38.92, 53.56])
# Example 3:
theta4 = np.array([-3, 1, 2, 3.5])
simple_predict(x, theta4)
# Output:
#array([12.5, 32. , 51.5, 71. ])