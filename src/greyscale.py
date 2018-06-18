import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

class grey():

	def brg2gray(self,pixel):
	#because opencv uses brg
		return (math.floor(0.114*pixel[0]+0.299*pixel[1]+0.587*pixel[2]))

	def convert_to_grey(self,img):
		width = img.shape[0]
		height = img.shape[1];
		gray = np.zeros((width+2,height+2))

		for i in range(0,width):
			for j in range(0,height):
				gray[i][j] = self.brg2gray(img[i][j])
		#print(grey[i][j])
		return gray

#img = cv.imread('test.jpg',cv.IMREAD_COLOR)
#to_grey=grey()
#gray=to_grey.convert_to_grey(img)
#plt.imshow(gray,cmap='gray',interpolation='bicubic')
#plt.show()