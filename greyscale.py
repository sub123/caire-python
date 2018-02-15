import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math


def brg2gray(pixel):
	return (math.floor(0.114*pixel[0]+0.299*pixel[1]+0.587*pixel[2]))

img = cv.imread('test.jpg',cv.IMREAD_COLOR)
cv.imshow("original",img)

width = img.shape[0]
height = img.shape[1];
grey = np.zeros((width,height))

for i in range(0,width):
	for j in range(0,height):
		grey[i][j] = brg2gray(img[i][j])
		#print(grey[i][j])

plt.imshow(grey,cmap='gray',interpolation='bicubic')
plt.show()