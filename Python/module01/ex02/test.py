class Values:
	def __set_name__(self, owner, name):
		self.private_name = '_' + name

	def __get__(self, obj, objtype=None):
		return getattr(obj, self.private_name)
	
	def __set__(self, obj, value):
		if all(isinstance(x, float) for x in value):
			setattr(obj, self.private_name, value)
		elif isinstance(value, int):
			setattr(obj, self.private_name, value)
		elif isinstance(value, range):
			setattr(obj, self.private_name, value)
		for lst in value:
			if all(isinstance(x, float) for x in lst):
				setattr(obj, self.private_name, value)
		print("Not valid values.")
class Vector:
	values = Values()

	def __init__(self, values):
		self.values = values
		self.shape = 4

v = Vector(3)