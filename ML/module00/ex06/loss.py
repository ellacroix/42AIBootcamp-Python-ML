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
	if x.ndim == 1:
		x = x.reshape((x.shape[0], 1))
	X = np.hstack((np.ones((x.shape[0],1)), x))
	return (np.dot(X, theta))

def simple_predict(x, theta):
	return np.array(theta[0] + x * theta[1]).astype(float)

def loss_elem_(y, y_hat):
	return (y_hat - y)**2

def loss_(y, y_hat):
	return np.mean(loss_elem_(y, y_hat))/2

x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
y_hat1 = predict_(x1, theta1)
y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
# Example 1:
print(loss_elem_(y1, y_hat1))
# Example 2:
print(loss_(y1, y_hat1))
x2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
theta2 = np.array([[0.05], [1.], [1.], [1.]])
y_hat2 = predict_(x2, theta2)
y2 = np.array([[19.], [42.], [67.], [93.]])
# Example 3:
print(loss_elem_(y2, y_hat2))
 # Example 4:
print(loss_(y2, y_hat2))
x3 = np.array([0, 15, -9, 7, 12, 3, -21])
theta3 = np.array([[0.], [1.]])
y_hat3 = predict_(x3, theta3)
y3 = np.array([2, 14, -13, 5, 12, 4, -19]).reshape(7,1)
# Example 5:
print(loss_(y3, y_hat3))
# Example 6:
print(loss_(y3, y3))