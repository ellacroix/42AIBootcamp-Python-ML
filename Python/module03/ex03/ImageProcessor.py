import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np

class ImageProcessor():

	def loadPIL(self, path):
		image = Image.open(path)
		image_array = np.array(image)
		print("Loading image of dimensions {} x {}".format(image.size[0], image.size[1]))
		return np.divide(image_array, 255)
		
	def displayPIL(self, array):
		array = np.multiply(array, 255)
		array = array.astype(np.uint8)
		img = Image.fromarray(array, 'RGB')
		img.show()

	def load(self, path):
		image = mpimg.imread(path)
		image = image[:,:,:-1]
		print("Loading image of dimensions {} x {}".format(image.shape[0], image.shape[1]))
		return image

	def display(self, array):
		plt.imshow(array)
		plt.show()

#imp = ImageProcessor()
#arrPIL = imp.loadPIL("42AI.png")
#arr = imp.load("42AI.png")
#imp.displayPIL(arrPIL)
#imp.display(arr)