import numpy as np
import matplotlib.pyplot as plt
import cv2

'''

First script studying Digital Image Processing with Python and OpenCV.
My basis is sentdex's youtube tutorial linked in the Readme file. All rights
goes to him and his great tutorials. 

'''
#IMREAD_UNCHANGED to read image as unchanged

img = cv2.imread('./test-images/test-img-1.jpg', cv2.IMREAD_GRAYSCALE)

#Showing image using only CV2
cv2.imshow('image', img)
cv2.waitKey(0) #waits for a key to be pressed
cv2.destroyAllWindows() #When key is pressed, destroy the window

#Showing image using Matplotlib
plt.imshow(img, cmap='gray', interpolation='bicubic')
#Since it's a matplotlib object, we can plot things over it
#We'll plot a random line over our image
plt.plot([80, 100], [1750, 1000], 'c', linewidth=5)
plt.show()

#Now, we can save the image on the directory we want by using the following command
cv2.imwrite('./test-images/test-img-1-out.jpg', img)
