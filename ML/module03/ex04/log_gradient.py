import numpy as np

def logistic_predict_(x, theta):
	y_hat = np.dot(np.c_[np.ones((len(x), 1)), x], theta)
	return 1 / (1 + np.exp(-y_hat))

def log_gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.array, with a for-loop.
    The three arrays must have compatible shapes.
    Args:
    x: has to be an numpy.array, a matrix of shape m * n.
    y: has to be an numpy.array, a vector of shape m * 1.
    theta: has to be an numpy.array, a vector (n +1) * 1.
    Return:
    The gradient as a numpy.array, a vector of shapes n * 1,
    containing the result of the formula for all j.
    None if x, y, or theta are empty numpy.array.
    None if x, y and theta do not have compatible shapes.
    None if x, y or theta is not of expected type.
    Raises:
    This function should not raise any Exception.
    """
    m = len(y)
    y_hat = logistic_predict_(x, theta)
    partial_derivative0 = sum(y_hat - y)/ m
    partial_derivative1 = sum((y_hat - y)*x)/ m
    return np.concatenate((partial_derivative0, partial_derivative1)).reshape(-1,1)

if __name__ == '__main__':
    y1 = np.array([1])
    x1 = np.array([4])
    theta1 = np.array([[2], [0.5]])
    print(log_gradient(x1, y1, theta1))
    # Example 2:
    y2 = np.array([[1], [0], [1], [0], [1]])
    x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
    theta2 = np.array([[2], [0.5]])
    print(log_gradient(x2, y2, theta2))
    # Example 3:
    y3 = np.array([[0], [1], [1]])
    x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
    theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
    print(log_gradient(x3, y3, theta3))