import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("messi5.jpg", cv2.IMREAD_GRAYSCALE)
#img = cv2.imread("sudoku.png", cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap));

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3) # 1 means we want to use the sobel func otherwise 0 -> 1 for dx and 0 for dy
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3) # 1 means we want to use the sobel func otherwise 0 -> 0 for dx and 1 for dy

sobelX = np.uint8(np.absolute(sobelX));
sobelY = np.uint8(np.absolute(sobelY));

canny = cv2.Canny(img, 100, 200)

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ("image", "Laplacian", "SobelX", "sobelY", "sobelCombined", "Canny");
images = [img, lap, sobelX, sobelY, sobelCombined, canny]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
