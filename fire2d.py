import cv2
import noise
import skfuzzy as fuzz

image = cv2.imread('lena.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
noise_image = noise.sp_noise(gray_image,0.02)
cv2.imwrite('noiseimg.png',noise_image)
fuzz_image = fuzz.filters.fire2d(noise_image, 0, 260,1)
cv2.imwrite('fireimg.png',fuzz_image)
