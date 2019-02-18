import os
import sys
from random import randint

import numpy as np
import cv2
import json


def main():
	
	windowName = 'Preview'
	fileName = 'photo.jpg'

	image = cv2.imread(fileName, cv2.IMREAD_UNCHANGED)
	# image = cv2.GaussianBlur(image, (3, 3), 0)

	cv2.namedWindow(windowName)

	while True:
		
		# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		gray = image
		
		# gray = cv2.GaussianBlur(gray, (13, 13), cv2.BORDER_DEFAULT)

		# b,g,r = cv2.split(gray)
		# blur = cv2.blur(r, (7, 7))
		# retval, mask = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
		# gray = cv2.bitwise_and(gray, gray, mask = mask)
		
		max = np.absolute(gray).max()
		gray = gray / max
		gray = np.round(gray)

		m = [255, 255, 255]
		
		gray = gray * m

		gray = np.uint8(gray)

		# _t = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
		# _r, _t = cv2.threshold(_t, 245, 255, cv2.THRESH_BINARY)
		# cv2.imshow('t', _t)

		

		# cv2.imwrite('gray.jpg', gray)
		# gray = cv2.imread('gray.jpg', cv2.IMREAD_UNCHANGED)

		# edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
		# gray = cv2.inpaint(gray, edges, 3, cv2.INPAINT_TELEA)

		# r, g, b = cv2.split(gray)
		# gray = cv2.merge([r, g, b])

		# # gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

		# degr = randint(15, 45)

		# rows = gray.shape[0]
		# cols = gray.shape[1]

		# M = cv2.getRotationMatrix2D((cols / 2, rows / 2), degr, 0.85)
		# gray = cv2.warpAffine(gray, M, (cols, rows))

		# параметры цветового фильтра
		hsv_min = np.array((0, 0, 0), np.uint8) #(0, 0, 255)
		hsv_max = np.array((2, 2, 2), np.uint8) #(0, 0, 255)

		hsv = cv2.cvtColor( gray, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV 
		thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр

		# ищем контуры и складируем их в переменную contours
		_, contours, hierarchy = cv2.findContours( thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

		# cv2.drawContours(gray, contours, -1, (255, 0, 0), 1)

		# # вычисляем моменты изображения
		# moments = cv2.moments(thresh, 1)
		# dM01 = moments['m01']
		# dM10 = moments['m10']
		# dArea = moments['m00']
		# # будем реагировать только на те моменты,
		# # которые содержать больше 100 пикселей
		# if dArea > 50:
		# 	x = int(dM10 / dArea)
		# 	y = int(dM01 / dArea)
		# 	cv2.circle(image, (x, y), 10, (0,0,255), -1)

		# перебираем все найденные контуры в цикле
		for cnt in contours:
			if len(cnt) == 3:
				rect = cv2.minAreaRect(cnt) # пытаемся вписать прямоугольник
				box = cv2.boxPoints(rect) # поиск четырех вершин прямоугольника
				box = np.int0(box) # округление координат
				# cv2.drawContours(gray, [box], 0, (255, 0, 0), 1) # рисуем прямоугольник

				M = cv2.moments(cnt)
				dM01 = M['m01']
				dM10 = M['m10']
				dArea = M['m00']
				# будем реагировать только на те моменты,
				# которые содержать больше 100 пикселей
				if dArea > 1:
					x = int(dM10 / dArea)
					y = int(dM01 / dArea)
					# (x,y), radius = cv2.minEnclosingCircle(cnt)
					cv2.circle(gray, (int(x), int(y)), 5, (255, 0, 0), -1)
					# gray = cv2.bitwise_and(gray, gray, mask = mask)


		# # отображаем контуры поверх изображения
		# #  cv2.drawContours( gray, contours, -1, (255,0,0), 1, cv2.LINE_AA, hierarchy, 1 )
		
		# # edges = cv2.Canny(gray, 0, 150, apertureSize = 3)
		# # gray = cv2.inpaint(gray, edges, 3, cv2.INPAINT_TELEA)
		gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
		cv2.imshow(windowName, gray)
		
		k = cv2.waitKey(40)
		if (k == 27 or k == 13):
			break



if __name__ == "__main__":
	main()

# import cv2
# import numpy as np

# def main():
# 	windowName = "Preview"
# 	cv2.namedWindow(windowName)
# 	cap = cv2.VideoCapture(0)
	
# 	if cap.isOpened():
# 		ret, frame = cap.read()
# 	else:
# 		ret = False


# 	while ret:
	
# 		ret, frame = cap.read()
		
# 		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		
# 		# Green Color
# 		# low = np.array([40, 50, 50])
# 		# high = np.array([80, 255, 255])
		
# 		# Blue Color
# 		# low = np.array([100, 50, 50])
# 		# high = np.array([140, 255, 255])
		
# 		# Red Color
# 		low = np.array([140, 150, 0])
# 		high = np.array([180, 255, 255])
		
# 		image_mask = cv2.inRange(hsv, low, high)
		
# 		output = cv2.bitwise_and(frame, frame, mask = image_mask)
		
# 		cv2.imshow("Original", frame)
# 		cv2.imshow("Mask", image_mask)
# 		cv2.imshow(windowName, output)
# 		if cv2.waitKey(1) == 27: # exit on ESC
# 			break

# 	cv2.destroyAllWindows()
# 	cap.release()
	
# main()