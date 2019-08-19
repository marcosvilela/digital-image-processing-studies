import cv2
import numpy as np

#Handles the main/first webcam of the system
cap = cv2.VideoCapture(0)
vidcap = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.avi', vidcap, 20.0, (640,480))

while True: #This loop applies every modification to every frame
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	out.write(frame) #Writes every frame of the original video
	cv2.imshow('frame', frame) #Original video feed
	cv2.imshow('gray', gray) #Modified video feed

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
out.release()
cv2.destroyAllWindows()		