import numpy as np
import cv2
from scipy.ndimage import uniform_filter

image = cv2.imread('son.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

kernel_size = 5

filtered_image = uniform_filter(image, size=kernel_size)

cv2.imwrite('filtered_image.jpg', cv2.cvtColor(filtered_image.astype(np.uint8), cv2.COLOR_RGB2BGR))
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()