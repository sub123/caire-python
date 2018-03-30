import cv2 as cv
import numpy as np
import sobel
import greyscale
import matplotlib.pyplot as plt

class caver():

	used_seams = []

	def __init__(self):


	def compute_seams(self,img):
		new_img = np.zeros([img.shape[0],img.shape[1]])
		to_grey = greyscale.grey()
		gray = to_grey.convert_to_grey(img)
		to_sobel = sobel()
		energy_map = to_sobel.get_sobel(gray,img.shape[0],img.shape[1])
		width = img.shape[0]
		height = img.shape[1]
		for i in range(width):
			new_img[0][i] = energy_map[0][i]
			new_img[height-1][i] = energy_map[height-1][i]

		for i in range(height):
			new_img[i][0] = energy_map[i][0]
			new_img[i][width-1] = energy_map[i][width-1]

		for i in range(1,width-1):
			for j in range(1,height-1):
				new_img[i][j] = min(min(new_img[i][j-1],new_img[i][j]),new_img[i][j+1])

		return new_img