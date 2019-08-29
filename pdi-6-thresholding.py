import cv2
import numpy as np 

'''

Thresholding: Extreme simplification of an image. A threshold means that
everything above (or below) its number is either 0 or 1 value.

We'll use an image of a book (courtesy of sentdex), with a low light and a curvature to it. It makes
it difficult to read what's written on it. 

'''

#Colored image
img = cv2.imread('./test-images/bookpage.jpg')

#Grayscaled image
img2 = cv2.imread('./test-images/bookpage.jpg')
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
Since we're using a low-light image, every pixel that's greater than 12
will be given the 255 value, turning into a black pixel.  

'''

#Thresholding a colored image gives us different shades of color
#We'll do it on a grayscaled image on the line below
retval, thresh = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
retval2, gray_thresh = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)


cv2.imshow('original', img)
cv2.imshow('grayscaled', grayscaled)
cv2.imshow('thresh', thresh)
cv2.imshow('thresh_grayscaled', gray_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''

Note that the b&w threshold got unreadable where the shadows on the image
are darker. We'll work now on something less straight-forward: A Gaussian
Adaptive Threshold.

It yields different thresholding results according to the image region it's
been applied. 

'''

gauss = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

'''
We'll see now that, using Adaptive Threshold, the shaded text is now
more clearly readable. 

'''
cv2.imshow('gauss', gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''

There's other thresholding algorithms that i'm going to append here
later on, like Otsu's binarization. We'll be saving every image on disk.

'''

cv2.imwrite('./test-images/thresh_gr_bookpage.jpg', gray_thresh)
cv2.imwrite('./test-images/thresh_bookpage.jpg', thresh)
cv2.imwrite('./test-images/gauss_thresh.jpg', gauss)