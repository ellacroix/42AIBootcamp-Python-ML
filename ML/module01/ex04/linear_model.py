import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt


data = pd.read_csv("are_blue_pills_magics.csv")
Xpill = np.array(data["Micrograms"]).reshape(-1,1)
Yscore = np.array(data["Score"]).reshape(-1,1)

# Example 1:
linear_model1 = MyLR(np.array([89.0, -8]))
"""Y_model1 = linear_model1.predict_(Xpill)
print(linear_model1.mse_(np.squeeze(Yscore), Y_model1))
print(mean_squared_error(Yscore, Y_model1))
linear_model1.fit_(Xpill, Yscore)
Y_model2 = linear_model1.predict_(Xpill)
plt.plot(Xpill, Yscore, 'o')
plt.plot(Xpill, Y_model1, "r--")
plt.plot(Xpill, Y_model2, color='green', marker='x', mew=3)
plt.plot(Xpill, Y_model2, "g--")
plt.show()"""

for theta0 in range(87, 91):
	linear_model1.thetas[0] = theta0
	loss_ = []
	for theta1 in np.arange(-14, -3.5, 0.5):
		linear_model1.thetas[1] = theta1
		loss_.append(linear_model1.mse_(np.squeeze(Yscore), linear_model1.predict_(Xpill)))
		#loss_.append(mean_squared_error(Yscore, linear_model1.predict_(Xpill)))
	plt.plot(np.arange(-14,-3.5, 0.5), loss_)
plt.show()


"""# Example 2:
linear_model2 = MyLR(np.array([89.0, -6]))
Y_model1 = linear_model2.predict_(Xpill)
print(linear_model2.mse_(Yscore, Y_model1))
print(mean_squared_error(Yscore, Y_model1))
linear_model2.fit_(Xpill, Yscore)
Y_model1 = linear_model2.predict_(Xpill)
plt.plot(Xpill, Yscore, 'o')
plt.plot(Xpill, Y_model1, "r--")
plt.plot(Xpill, Y_model2, color='green', marker='x', mew=3)
plt.plot(Xpill, Y_model2, "g--")
plt.show()"""