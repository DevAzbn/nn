import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#load cascade classifier training file for haarcascade
	#cascade = cv2.CascadeClassifier('C:/Users/azbn/AppData/Local/OpenCV/opencv/build/etc/haarcascades/haarcascade_frontalface_alt.xml')
	#cascade2 = cv2.CascadeClassifier('C:/Users/azbn/AppData/Local/OpenCV/opencv/build/etc/haarcascades/haarcascade_eye.xml')
	#(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
	#faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
	#eyes = cascade2.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
	#if len(faces):
	#	for (x, y, w, h) in faces:
	#		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	#if len(eyes):
	#	for (x, y, w, h) in eyes:
	#		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

	# Display the resulting frame
	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()