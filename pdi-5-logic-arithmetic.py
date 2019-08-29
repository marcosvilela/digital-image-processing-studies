import cv2
import numpy as np

background = cv2.imread('./test-images/mark.jpg')
img2 = cv2.imread('./test-images/logo.png')

#Saves the size (rows and columns) of the image
rows, cols, channels = img2.shape
roi = background[0:rows, 0:cols]


#Mask used on the operation is normally the image converted to grayscale
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

#Invisible part of the mask: This is the area where there is no mask
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

finalimg = cv2.add(img1_bg, img2_fg)


cv2.imshow('img', img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()