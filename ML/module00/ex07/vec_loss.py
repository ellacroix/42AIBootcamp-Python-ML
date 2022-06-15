import numpy as np

def loss_(y, y_hat):
	return ((y_hat - y)**2).mean()/2



X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
#X = np.array([[0.], [15.], [-9.], [7], [12.], [3.], [-21]])
#Y = np.array([[2.], [14.], [-13.], [5.], [12.], [4.], [-19]])
# Example 1:
print(loss_(X, Y))
# Example 2:
print(loss_(X, X))