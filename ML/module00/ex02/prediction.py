import numpy as np

def simple_predict(x, theta):
	return np.array(theta[0] + x * theta[1]).astype(float)


x = np.arange(1,6)
# Example 1:
theta1 = np.array([5, 0])
print(simple_predict(x, theta1))
# Example 2:
theta2 = np.array([0, 1])
print(simple_predict(x, theta2))
# Example 3:
theta3 = np.array([5, 3])
print(simple_predict(x, theta3))
# Example 4:
theta4 = np.array([-3, 1])
print(simple_predict(x, theta4))