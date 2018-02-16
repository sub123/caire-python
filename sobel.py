import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

kernelX = [[-1,0,1],[-2,0,2],[-1,0,1]]
kernelY = [[-1,-2,-1],[0,0,0],[1,2,1]]


def brg2gray(pixel):
	#because opencv uses brg
	return (math.floor(0.114*pixel[0]+0.299*pixel[1]+0.587*pixel[2]))

img = cv.imread('test.jpg',cv.IMREAD_COLOR)
cv.imshow("original",img)

width = img.shape[0]
height = img.shape[1];
grey = np.zeros((width+2,height+2))

for i in range(0,width):
	for j in range(0,height):
		grey[i][j] = brg2gray(img[i][j])
		#print(grey[i][j])

plt.imshow(grey,cmap='gray',interpolation='bicubic')
plt.show()

threshold=10

def sobel():
	sobel = np.zeros((width,height))
	for i in range(1,width):
		for j in range(1,height):
			x=kernelX[0][0]*grey[i-1][j-1]+kernelX[0][1]*grey[i-1][j]+kernelX[0][2]*grey[i-1][j+1]+kernelX[1][0]*grey[i][j-1]+kernelX[1][1]*grey[i][j]+kernelX[1][2]*grey[i][j+1]+kernelX[2][0]*grey[i+1][j-1]+kernelX[2][1]*grey[i+1][j]+kernelX[2][2]*grey[i+1][j+1]
			y=kernelY[0][0]*grey[i-1][j-1]+kernelY[0][1]*grey[i-1][j]+kernelY[0][2]*grey[i-1][j+1]+kernelY[1][0]*grey[i][j-1]+kernelY[1][1]*grey[i][j]+kernelY[1][2]*grey[i][j+1]+kernelY[2][0]*grey[i+1][j-1]+kernelY[2][1]*grey[i+1][j]+kernelY[2][2]*grey[i+1][j+1]
			magnitude = (int)(math.sqrt(x*x+y*y))
			if(magnitude<0):
				magnitude=0
			elif magnitude>255:
				magnitude=255
			if magnitude<threshold:
				magnitude=0
			sobel[i][j]=magnitude
	plt.imshow(sobel,cmap='gray',interpolation='bicubic')
	plt.show()
sobel()