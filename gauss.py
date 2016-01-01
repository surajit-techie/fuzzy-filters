import cv2
import noise
import scipy.ndimage

image = cv2.imread('lena.jpg')
noise_image = noise.sp_noise(image,0.02)
cv2.imwrite('noiseimg.png',noise_image)
gauss_image = scipy.ndimage.filters.gaussian_filter(noise_image, sigma=2, order=0, output=None, mode='reflect', cval=0.0)
cv2.imwrite('gaussimg.png',gauss_image)
