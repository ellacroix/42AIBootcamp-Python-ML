

class Matrix():

	def __init__(self, data):
		if type(data) == list:
			self.data = data
			self.shape = (len(data), len(data[0]))
		elif type(data) == tuple:
			self.data = []
			for a in range (0, data[0]):
				array = [0] * data[1]
				self.data.append(array)
			self.shape = data
	
	def __add__(self, other):
		if self.shape != other.shape:
			raise ValueError("Matrices have to be of the same dimensions")
		res = []
		for r in range(0, self.shape[0]):
			array = []
			for c in range(0, self.shape[1]):
				array.append(self.data[r][c] + other.data[r][c])
			res.append(array)
		return Matrix(res)
	
	def __radd__(self, other):
		return self.__add__(other)

	def __sub__(self, other):
		if self.shape != other.shape:
			raise ValueError("Matrices have to be of the same dimensions")
		res = []
		for r in range(0, self.shape[0]):
			array = []
			for c in range(0, self.shape[1]):
				array.append(self.data[r][c] - other.data[r][c])
			res.append(array)
		return Matrix(res)
	
	def __rsub__(self, other):
		return self.__sub__(other)

	def	__truediv__(self, scalar):
		if scalar == 0:
			print("Division by 0")
			pass
		res = []
		for r in range(0, self.shape[0]):
			array = []
			for c in range(0, self.shape[1]):
				array.append(self.data[r][c] / scalar)
			res.append(array)
		return Matrix(res)
	
	def	__rtruediv__(self, scalar):
		return self.__truediv__(scalar)

	def __mul__(self, other):
		if  isinstance(other, (float, int)):
			res = []
			for r in range(0, self.shape[0]):
				array = []
				for c in range(0, self.shape[1]):
					array.append(self.data[r][c] * other)
				res.append(array)
			return Matrix(res)
		elif other.shape[1] == 1:
			if self.shape[1] != other.shape[0]:
				raise ValueError("Matrix and vector dimensions do not fit")
			res = []
			for r in range(0, self.shape[0]):
				addition = 0
				for c in range(0, self.shape[1]):
					addition += self.data[r][c] * other.data[c][0]
				res.append(addition)
			return Vector(res)
		elif isinstance(other, Matrix):
			if self.shape[1] != other.shape[0]:
				raise ValueError("Matrixes dimensions do not fit")
			res = []
			for r in range(0, self.shape[0]):
				row = []
				for c in range(0, other.shape[1]):
					f = 0
					for i in range(0, other.shape[0]):
						f += self.data[r][i] * other.data[i][c]
					row.append(f)
				res.append(row)
		return Matrix(res)

	def __rmul__(self, other):
		return self.__mul__(other)

	def T(self):
		res = []
		for c in range(0, self.shape[1]):
			row = []
			for r in range(0, self.shape[0]):
				print(self.data[r][c])
				row.append(self.data[r][c])
			res.append(row)
		return(Matrix(res))

	def __str__(self):
		return "Data:" + str(self.data) + ", Shape:" + str(self.shape)

	def __repr__(self):
		return "%s(%r)" % (self.__class__, self.__dict__)

class Vector(Matrix):

	def __init__(self, vector):
		self.data = vector
		self.shape = (len(vector), 1)
	
	def dot(self, other):
		if self.shape != other.shape:
			raise ValueError("Vectors have to be of the same shape")
		res = 0
		for r in range(0, self.shape[0]):
			res += (self.data[r][0] * other.data[r][0])
		return(res)

m1 = Matrix([	[0.0, 1.0, 2.0, 3.0],
				[0.0, 2.0, 4.0, 6.0]])
m2 = Matrix((2,3))
m3 = Matrix([	[0.0, 1.0],
				[2.0, 3.0],
				[4.0, 5.0],
				[6.0, 7.0]])
v1 = Vector([[1], [2], [3], [4]])
v2 = Vector([[1], [2], [3]])
v3 = Vector([[2], [4], [8]])
#print(m1.__dict__)
#print(m2.__dict__)
#print(v1.__dict__)
#print((m1 + m1).__dict__)
#print((v1 + v1).__dict__)
#print((m1 - m1).__dict__)
#print((m1 / 2).__dict__)
#print((2 / m1).__dict__)
#print((m1 * 2).__dict__)
#print((m1 * v1).__dict__)
#print((m1 * m3).__dict__)
#print((m1 * m3))
#print(repr(v1))
#print(m3.T())
#print(v2.dot(v3))