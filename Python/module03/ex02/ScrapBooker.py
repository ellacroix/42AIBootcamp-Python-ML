import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class ScrapBooker():

	def crop(self, array, dim, position=(0,0)):
		sy = position[0]
		ey = position[0] + dim[0]
		sx = position[1]
		ex = position[1] + dim[1]
		if ex > len(array) or ey > len(array[0]):
			print("Error, array is too small.")
			return None
		return array[sy:ey,sx:ex]

	def thin(self, array, n, axis):
		if axis:
			return (np.delete(array, slice(n-1, None, n), 0))
		else:
			return (np.delete(array, slice(n-1, None, n), 1))

	def juxtapose(self, array, n, axis):
		if axis:
			return np.tile(array, n)
		else:
			return np.tile(array, (n,1))

	def mosaic(self, array, dim):
		array = ScrapBooker.juxtapose(self, array, dim[0], 0)
		return ScrapBooker.juxtapose(self, array, dim[1], 1)

spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
#print(arr1)
print(spb.crop(arr1, (3,2),(0,0)))
arr2 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
print(arr2)
print(spb.thin(arr2,4,0))
arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
#print(arr3)
#print(spb.juxtapose(arr3, 3, 0))
arr4 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
#print(arr4)
#print(spb.mosaic(arr4, (2,4)))
