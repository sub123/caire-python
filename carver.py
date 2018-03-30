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