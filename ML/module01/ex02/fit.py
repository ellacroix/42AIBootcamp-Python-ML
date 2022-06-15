import numpy as np

def predict_(x, theta):
	X = np.c_[np.ones((len(x), 1)), x]
	return (np.dot(X, theta))

def gradient(x, y, theta):
	X = np.c_[np.ones((len(x), 1)), x]
	y = np.squeeze(y)
	y_hat = np.dot(X, theta)
	#print("{} . {} = {}".format(X, theta, y_hat))
	return np.dot(np.transpose(X),(y_hat - y))/len(x)

def fit_(x, y, theta, alpha, max_iter):
	"""
	Description:
	Fits the model to the training dataset contained in x and y.
	Args:
	x: has to be a numpy.array, a vector of shape m * 1: (number of training examples, 1).
	y: has to be a numpy.array, a vector of shape m * 1: (number of training examples, 1).
	theta: has to be a numpy.array, a vector of shape 2 * 1.
	alpha: has to be a float, the learning rate
	max_iter: has to be an int, the number of iterations done during the gradient descent
	Return:
	new_theta: numpy.array, a vector of shape 2 * 1.
	None if there is a matching shape problem.
	None if x, y, theta, alpha or max_iter is not of the expected type.
	Raises:
	This function should not raise any Exception.
	"""
	for i in range(0, max_iter):
		grad = gradient(x, y, theta)
		theta = theta - alpha * grad
	return theta.reshape(len(theta),1)


x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
#x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
#y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])
theta = np.array([1, 1])
# Example 0:
theta1 = fit_(x, y, theta, alpha=5e-6, max_iter=15000)
print(theta1)
# Output:
#array([[1.40709365],
#		[1.1150909 ]])

# Example 1:
print(predict_(x, theta1))
# Output:
#array([[15.3408728 ],
#		[25.38243697],
#		[36.59126492],
#		[55.95130097],
#		[65.53471499]])
