from ImageProcessor import ImageProcessor
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class ColorFilter():
	@staticmethod
	def invert(array):
		return 1 - array

	@staticmethod
	def to_blue(array):
		blue = np.zeros(array.shape)
		blue[:,:,2] = array[:,:,2]
		return blue

	@staticmethod
	def to_green(array):
		return array * [0, 1, 0]

	@staticmethod
	def to_red(array):
		return array - cf.to_blue(array) - cf.to_green(array)

	@staticmethod
	def to_celluloid(array):
		new = np.copy(array)
		hold = np.linspace(1.0, 0.0, num=5, endpoint=True)
		print(hold)
		for i in hold:
			indexes = array >= i
			array[indexes] = -1
			new[indexes] = i
		return new
	
	@staticmethod
	def to_grayscale(array, filter):
		return array

imp = ImageProcessor()
arr = imp.load("/mnt/nfs/homes/ellacroi/Desktop/bootcamp-python/module03/ex03/elon_canaGAN.png")
cf = ColorFilter()
#inv = cf.invert(arr)
#imp.display(inv)
#blue = cf.to_blue(arr)
#imp.display(blue)
#green = cf.to_green(arr)
#imp.display(green)
#red = cf.to_red(arr)
#imp.display(red)
#cell = cf.to_celluloid(arr)
#imp.display(cell)
gray = cf.to_grayscale(arr, 'm')
imp.display(gray)