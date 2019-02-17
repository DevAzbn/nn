import os
import sys

import numpy as np
import cv2
import json


args = sys.argv


params = ['--project=']


drawing = False
(x0, y0, x1, y1) = (-1, -1, -1, -1)
image, image_, image__, rimage = None, None, None, None
project = ''
actfile = ''
dpath = ''
result = {}


def draw_shape(event, x, y, flags, param):
	global x0, y0, x1, y1, drawing, image, image_, image__, rimage, actfile, result, dpath

	alpha = 0.5
	
	if event == cv2.EVENT_LBUTTONDOWN:
		if drawing == False:
			drawing = True
			(x0, y0) = x, y
			(x1, y1) = x, y
			image__ = image.copy()
			rimage = image__

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			(x1, y1) = x, y
			if(x1 > image.shape[1]):
				x1 = image.shape[1]
			if(y1 > image.shape[0]):
				y1 = image.shape[0]
			if (x1 > x0) & (y1 > y0):
				
				image__ = image.copy()
				cv2.rectangle(image__, (x0, y0), (x1, y1), (0, 255, 0), 0)
				rimage = image__
				
				# gray = cv2.cvtColor(image__, cv2.COLOR_BGR2GRAY)
				# blurred = cv2.bilateralFilter(gray, 9, 75, 75)
				# image__ = cv2.addWeighted(gray, 1.5, blurred, -0.5, 0)

			# if mode == True:
			# 	cv2.rectangle(image, (ix, iy), (x, y), (0, 255, 0), -1)
			# else:
			# 	cv2.circle(image, (x, y), 5, (0, 0, 255), -1)

	elif event == cv2.EVENT_LBUTTONUP:
		if drawing == True:
			(x1, y1) = x, y
			if(x1 > image.shape[1]):
				x1 = image.shape[1]
			if(y1 > image.shape[0]):
				y1 = image.shape[0]
			drawing = False
			print(x0, y0, x1, y1)
			cv2.rectangle(image_, (x0, y0), (x1, y1), (0, 0, 255), 2)
			rimage = image_
			result[actfile].append([(x0, y0), (x1, y1)]) #, (x1 - x0, y1 - y0)
			#cv2.imwrite("{}_{}_{}_{}_{}.jpg".format(actfile, x0, y0, x1, y1), image[y0:y1, x0:x1])
			cv2.imwrite(dpath + "/cache/{}_{}.jpg".format(actfile, len(result[actfile])), image[y0:y1, x0:x1])
		# drawing = False
		# if mode == True:
		# 	cv2.rectangle(image, (ix, iy), (x, y), (0, 255, 0), -1)
		# else:
		# 	cv2.circle(image, (x, y), 5, (0, 0, 255), -1)

def main(d):
	global x0, y0, x1, y1, drawing, image, image_, image__, rimage, actfile, result, dpath

	prefix = './projects/'
	dpath = prefix + d
	files = os.listdir(dpath + '/pos')
	files = filter(lambda x: x.endswith('.jpg') or x.endswith('.png'), files)

	for f in files:
		actfile = f
		filename = dpath + '/pos/' + f
		print(filename)
		result[f] = []

		windowName = filename

		image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)



		# # параметры цветового фильтра
		# hsv_min = np.array((0, 45, 170), np.uint8)
		# hsv_max = np.array((35, 105, 250), np.uint8)

		# hsv = cv2.cvtColor( image, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV 
		# thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр

		# # ищем контуры и складируем их в переменную contours
		# _, contours, hierarchy = cv2.findContours( thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

		# # # вычисляем моменты изображения
		# # moments = cv2.moments(thresh, 1)
		# # dM01 = moments['m01']
		# # dM10 = moments['m10']
		# # dArea = moments['m00']
		# # # будем реагировать только на те моменты,
		# # # которые содержать больше 100 пикселей
		# # if dArea > 50:
		# # 	x = int(dM10 / dArea)
		# # 	y = int(dM01 / dArea)
		# # 	cv2.circle(image, (x, y), 10, (0,0,255), -1)

		# # перебираем все найденные контуры в цикле
		# for cnt in contours:
		# 	if(len(cnt) < 100):
		# 		rect = cv2.minAreaRect(cnt) # пытаемся вписать прямоугольник
		# 		box = cv2.boxPoints(rect) # поиск четырех вершин прямоугольника
		# 		box = np.int0(box) # округление координат
		# 		cv2.drawContours(image,[box],0,(255,0,0),2) # рисуем прямоугольник

		# # отображаем контуры поверх изображения
		# # cv2.drawContours( image, contours, -1, (255,0,0), 1, cv2.LINE_AA, hierarchy, 1 )

		# #image = thresh




		image_ = image.copy()
		image__ = image.copy()
		rimage = image_

		cv2.namedWindow(windowName)

		drawing = False
		(x0, y0, x1, y1) = (-1, -1, -1, -1)

		cv2.setMouseCallback(windowName, draw_shape)

		while(True):
			cv2.imshow(windowName, rimage)
			k = cv2.waitKey(25)
			if k == 13:
				break
			elif k == 27:
				sys.exit()
			# 	# else:
			# 	# 	print(k) enter = 13 esc = 27
			# 	# elif k == 20:
			# 	# 	pass
			# 	# if k == ord('m') or k == ord('M'):
		with open(dpath + '/marked.json', 'w') as fi:
			json.dump(result, fi, ensure_ascii = False)
		str = ''
		for l in result:
			# for i in result[l]:
			# 	str = str + "./pos/{} 1 {} {} {} {}".format(l, i[0][0], i[0][1], i[1][0] - i[0][0], i[1][1] - i[0][1]) + "\n"
			
			lcoord = ''
			for i in result[l]:
				lcoord = lcoord + " {} {} {} {}".format(i[0][0], i[0][1], i[1][0] - i[0][0], i[1][1] - i[0][1])
			str = str + dpath + "/pos/{} {}{}".format(l, len(result[l]), lcoord) + "\n"
			
		with open(dpath + '/pos.txt', 'w') as fi:
			fi.write(str)
		cv2.destroyAllWindows()


if __name__ == "__main__":
	for a in args:
		if a.startswith(params[0]):
			dir = a[len(params[0]):]
			main(dir)