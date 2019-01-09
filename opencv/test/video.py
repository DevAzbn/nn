import numpy as np
import cv2

final_wide = 300
dim = 0

#красный цвет представляет из себя две области в пространстве HSV
lower_color = np.array([0, 85, 85], dtype = "uint8")
upper_color = np.array([180, 255, 255], dtype = "uint8")

#красный в диапазоне фиолетового оттенка
lower_color2 = np.array([165, 85, 110], dtype = "uint8")
upper_color2 = np.array([180, 255, 255], dtype = "uint8")

video_file = 'Y:\Video\Svyaz.avi'	 #указываем имя файла в переменной, 
cap = cv2.VideoCapture(video_file)	  #для последующего автоматического перебора файлов

while(cap.isOpened()):
	ret, frame = cap.read() #получаем кадр из видеопотока
	if frame is None:   #проверка на корректность кадра
		break
	if not dim:
		r = float(final_wide) / frame.shape[1]
		dim = (final_wide, int(frame.shape[0] * r))
	
	resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

	resized_gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) #Преобразуем в GRAY

	#load cascade classifier training file for haarcascade
	#cascade = cv2.CascadeClassifier('C:/Users/azbn/AppData/Local/OpenCV/opencv/build/etc/haarcascades/haarcascade_frontalface_alt.xml')
	#cascade2 = cv2.CascadeClassifier('C:/Users/azbn/AppData/Local/OpenCV/opencv/build/etc/haarcascades/haarcascade_eye.xml')
	#faces = cascade.detectMultiScale(resized_gray, scaleFactor=1.1, minNeighbors=5)
	#if len(faces):
	#	for (x, y, w, h) in faces:
	#		cv2.rectangle(resized, (x, y), (x+w, y+h), (0, 255, 0), 2)
	
	#resized_gray = cv2.GaussianBlur(resized_gray, (3, 3), 0)
	#resized_gray = cv2.Canny(resized_gray, 25, 250)

	#resized = cv2.bilateralFilter(resized, 75, 75, 75)

	#Чтобы убрать промежутки между белыми пикселями изображения, мы применим операцию «закрытия»:
	#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
	#resized = cv2.morphologyEx(resized, cv2.MORPH_CLOSE, kernel)

	#cnts = cv2.findContours(resized_gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
	#for c in cnts:
	#	peri = cv2.arcLength(c, True)
	#	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	#	if len(approx) > 6:
	#		cv2.drawContours(resized, [approx], -1, (0, 255, 0), 4)

	#resized_hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV) #Преобразуем в HSV

	#mask1 = cv2.inRange(resized_hsv, lower_color, upper_color)        #применяем маску по цвету
	#mask2 = cv2.inRange(resized_hsv, lower_color2, upper_color2)  #для красного таких 2
	
	#mask_full = mask1 + mask2 #полная масква предствавляет из себя сумму

	cv2.imshow("video_frame", resized)	#показываем кадр в opencv окне
	
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break   #в случае нажатия клавиши q выходим из цикла
	
cap.release()
cv2.waitKey(1); #костыль для закрытия окна, может быть нужен в jupyter
cv2.destroyAllWindows()