import cv2
import numpy as np

img = cv2.imread('./test-images/test-img-1.jpg', cv2.IMREAD_COLOR)


#Draws a line
cv2.line(img, (0,0), (150, 150), (255,255,255), 15)
#Draws a rectangle
cv2.rectangle(img, (15,25), (200,150), (0, 255, 0), 5)
#Draws a circle
cv2.circle(img, (100,63), 55, (0, 0, 255), -1)

#Points used to close a polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
cv2.polylines(img, [pts], True, (0, 255, 255), 3)


#Writing text on the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tutorial!', (0, 500), font, 1, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('./test-images/test-img-3-out.jpg', img)
