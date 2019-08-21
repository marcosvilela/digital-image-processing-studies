import cv2
import numpy as np

img = cv2.imread('./test-images/test-img-1.jpg', cv2.IMREAD_COLOR)
px = img[55,55] #Pixel with coordinates [55, 55]. The variable stores the pixel's color values.
print(px)

img[55, 55] = [0, 0, 0] #This line modifies the color values of that single pixel
print(px)

'''

ROI = Region of Interest; A set of pixels contained within the original
image that forms a subimage.

'''
roi = img[100:500, 100:500] 
print(img) #Prints the color values of all pixels inside the ROI

#Convert all color values inside the ROI to black, creating a black square
#that highlights the region if interest
img[100:500, 100:500] = [0, 0, 0]
#We save the image with the highlighted ROI for example
cv2.imwrite('./test-images/roi-sample.jpg', img)

#We can also move the ROI around the image by changing another ROI into it
mov_roi = img[37:111, 107:194]
img[0:74, 0:87] = mov_roi
cv2.imwrite('./test-images/translted_img.jpg', img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()