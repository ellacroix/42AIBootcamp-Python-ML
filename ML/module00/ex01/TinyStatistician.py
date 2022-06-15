import numpy as np
import math


class TinyStatistician():

	def mean(self, x):
		return sum(x)/len(x)

	def percentile(self, x, p):
		n = int(round((p/100) * len(x) + 0.5))
		return float(x[n-1])

	def median(self, x):
		x.sort()
		mid = len(x) // 2
		return (x[mid] + x[~mid]) / 2

	def quartile(self, x):
		res = []
		res.append(self.percentile(x, 25))
		res.append(self.percentile(x, 75))
		return res

	def var(self, x):
		mean = self.mean(x)
		res = 0.0
		for n in x:
			res += (n-mean)**2
		return res/len(x)

	def std(self, x):
		return math.sqrt(self.var(x))

a = [1, 42, 300, 10, 59]
#a = np.array(a)
stat = TinyStatistician()
print(stat.mean(a))
print(stat.median(a))
print(stat.quartile(a))
print(stat.percentile(a, 10))
print(stat.percentile(a, 50))
print(stat.percentile(a, 83))
print(stat.var(a))
print(stat.std(a))