import cv2

img = cv2.imread('baboon.jpg', 0)
#_, threshold = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
# adaptive_threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 2)
adaptive_threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 2)
cv2.imshow('Image', img)
cv2.imshow('Threshold', adaptive_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
