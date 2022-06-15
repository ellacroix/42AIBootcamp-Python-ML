import numpy as np


class MyLinearRegression():
	"""
	Description:
	My personnal linear regression class to fit like a boss.
	"""
	def __init__(self, thetas, alpha=0.001, max_iter=1000):
		self.alpha = alpha
		self.max_iter = max_iter
		self.thetas = thetas


	def predict_(self, x):
		return np.dot(np.c_[np.ones((len(x), 1)), x], self.thetas)

	def gradient(self, x, y, theta):
		X = np.c_[np.ones((len(x), 1)), x]
		y = np.squeeze(y)
		y_hat = np.dot(X, theta)
		return np.dot(np.transpose(X),(y_hat - y))/len(x)

	def fit_(self, x, y):
		for i in range(0, self.max_iter):
			grad = self.gradient(x, y, self.thetas)
			self.thetas = self.thetas - self.alpha * grad
		return self.thetas

	def loss_elem_(self, y_hat, y):
		m = len(y)
		y = np.squeeze(y)
		return (((y_hat - y) ** 2) / (2 * m))

	def loss_(self, y_hat, y):
		elem = self.loss_elem_(y_hat, y)
		return sum(elem)

"""x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
lr1 = MyLinearRegression([2, 0.7])
# Example 0.0:
print(lr1.predict_(x))
# Example 0.1:
print(lr1.loss_elem_(lr1.predict_(x),y))
# Example 0.2:
print(lr1.loss_(lr1.predict_(x),y))

# Example 1.0:
lr2 = MyLinearRegression([1, 1], 5e-6, 15000)
print(lr2.fit_(x, y))
print(lr2.thetas)
# Example 1.1:
print(lr2.predict_(x))
# Example 1.2:
print(lr2.loss_elem_(lr2.predict_(x),y))
# Example 1.3:
print(lr2.loss_(lr2.predict_(x),y))"""