import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math
import greyscale

class sobel():

	kernelX = [[-1,0,1],[-2,0,2],[-1,0,1]]
	kernelY = [[-1,-2,-1],[0,0,0],[1,2,1]]


	threshold=10

	def get_sobel(self,grey,width,height):
		sobel = np.zeros((width,height))
		for i in range(1,width):
			for j in range(1,height):
				x=self.kernelX[0][0]*grey[i-1][j-1]+self.kernelX[0][1]*grey[i-1][j]+self.kernelX[0][2]*grey[i-1][j+1]+self.kernelX[1][0]*grey[i][j-1]+self.kernelX[1][1]*grey[i][j]+self.kernelX[1][2]*grey[i][j+1]+self.kernelX[2][0]*grey[i+1][j-1]+self.kernelX[2][1]*grey[i+1][j]+self.kernelX[2][2]*grey[i+1][j+1]
				y=self.kernelY[0][0]*grey[i-1][j-1]+self.kernelY[0][1]*grey[i-1][j]+self.kernelY[0][2]*grey[i-1][j+1]+self.kernelY[1][0]*grey[i][j-1]+self.kernelY[1][1]*grey[i][j]+self.kernelY[1][2]*grey[i][j+1]+self.kernelY[2][0]*grey[i+1][j-1]+self.kernelY[2][1]*grey[i+1][j]+self.kernelY[2][2]*grey[i+1][j+1]
				magnitude = (int)(math.sqrt(x*x+y*y))
				if(magnitude<0):
					magnitude=0
				elif magnitude>255:
					magnitude=255
				if magnitude<self.threshold:
					magnitude=0
				sobel[i][j]=magnitude
		return sobel

#img = cv.imread('test.jpg',cv.IMREAD_COLOR)
#to_grey=greyscale.grey()
#gray=to_grey.convert_to_grey(img)
#to_sobel=sobel()
#energy_map=to_sobel.get_sobel(gray,img.shape[0],img.shape[1])
#plt.imshow(energy_map,cmap='gray',interpolation='bicubic')
#plt.show()