import os
import cv2
import random
import numpy as np
import skfuzzy as fuzz

def sp_noise(image,prob):
	output = np.zeros(image.shape,np.uint8)
	thres = 1 - prob 
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			rdn = random.random()
			if rdn < prob:
				output[i][j] = 0
			elif rdn > thres:
				output[i][j] = 255
			else:
				output[i][j] = image[i][j]
	return output

image = cv2.imread('lena.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
noise_image = sp_noise(gray_image,0.02)
cv2.imwrite('noiseimg.png',noise_image)
fuzz_image = fuzz.filters.fire2d(noise_image, 0, 260,1)
cv2.imwrite('fuzzimg.png',fuzz_image)
