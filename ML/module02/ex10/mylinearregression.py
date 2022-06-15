import numpy as np


class MyLinearRegression:

	def __init__(self, thetas, alpha=0.001, max_iter=1000):
		self.alpha = alpha
		self.max_iter = max_iter
		self.thetas = thetas


	def predict_(self, x):
		X = np.c_[np.ones((len(x), 1)), x]
		#print("x:{}".format(x))
		#print("X:{}".format(X))
		y_hat = np.dot(X, self.thetas)
		#print(y_hat.reshape((len(x), -1)))
		return y_hat
		#return y_hat.reshape((len(x), -1))

	def gradient_(self, x, y, theta):
		X = np.c_[np.ones((len(x), 1)), x]
		#y = np.squeeze(y)
		y_hat = np.dot(X, theta)
		return np.dot(np.transpose(X),(y_hat - y))/len(x)

	def fit_(self, x, y):
		#print("x:{}".format(x))
		#print("y:{}".format(y))
		print(self.gradient_(x, y, self.thetas))
		for i in range(0, self.max_iter):
			grad = self.gradient_(x, y, self.thetas)
			self.thetas = self.thetas - self.alpha * grad
			#if i%10000 == 0: print(sum(grad))
		return self.thetas
	
	def mse_(self, y, y_hat):
		#print("y:{}".format(y))
		#print("y_hat:{}".format(y_hat))
		return float(sum((y_hat - y) ** 2)/(len(y)))
		#return np.dot((y_hat - y),(y_hat - y))/len(y)

if __name__ == '__main__':
	X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89., 144.]])
	Y = np.array([[23.], [48.], [218.]])
	mylr = MyLinearRegression([[1.], [1.], [1.], [1.], [1]])
	#print("X:{}".format(X))
	# Example 0:
	#print("predict(X):\n{}".format(mylr.predict_(X)))
	# Example 2:
	#print("mse_(Y, y_hat):{}".format(mylr.mse_(Y, mylr.predict_(X))))
	# Example 3:
	mylr.alpha = 1.6e-4
	mylr.max_iter = 20000
	#print("gradient:{}".format(mylr.gradient_(X, Y, mylr.thetas)))
	mylr.fit_(X, Y)
	print("fit(X,Y), thetas => \n{}".format(mylr.thetas))
	#mylr.theta
	# Output:
	#array([[18.188..], [2.767..], [-0.374..], [1.392..], [0.017..]])
	# Example 4:
	#print("predict(X):\n{}".format(mylr.predict_(X)))
	# Output:
	#array([[23.417..], [47.489..], [218.065...]])
	#print("mse_(Y, y_hat):{}".format(mylr.mse_(Y, mylr.predict_(X))))
	# Output:
	#0.0732 * 2..