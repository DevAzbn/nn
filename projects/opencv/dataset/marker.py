import numpy as np
import cv2

windowName = 'Drawing Demo'
image = cv2.imread('neo.jpg', cv2.IMREAD_UNCHANGED)
image_ = image.copy()
image__ = image.copy()
rimage = image_

cv2.namedWindow(windowName)

# true if mouse is pressed
drawing = False
(x0, y0, x1, y1) = (-1, -1, -1, -1)

def draw_shape(event, x, y, flags, param):
	global x0, y0, x1, y1, drawing, image, image_, rimage

	if event == cv2.EVENT_LBUTTONDOWN:
		if drawing == False:
			drawing = True
			(x0, y0) = x, y
			(x1, y1) = x, y
			rimage = image__

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			(x1, y1) = x, y
			if (x1 > x0) & (y1 > y0):
				cv2.rectangle(image__, (x0, y0), (x1, y1), (0, 255, 0, 0.5), -1)
			# if mode == True:
			# 	cv2.rectangle(image, (ix, iy), (x, y), (0, 255, 0), -1)
			# else:
			# 	cv2.circle(image, (x, y), 5, (0, 0, 255), -1)

	elif event == cv2.EVENT_LBUTTONUP:
		if drawing == True:
			(x1, y1) = x, y
			drawing = False
			print(x0, y0, x1, y1)
			cv2.rectangle(image_, (x0, y0), (x1, y1), (0, 255, 0, 0.5), 0)
			rimage = image_
			cv2.imwrite("{}_{}_{}_{}.jpg".format(x0, y0, x1, y1), image[y0:y1, x0:x1])
		# drawing = False
		# if mode == True:
		# 	cv2.rectangle(image, (ix, iy), (x, y), (0, 255, 0), -1)
		# else:
		# 	cv2.circle(image, (x, y), 5, (0, 0, 255), -1)

cv2.setMouseCallback(windowName, draw_shape)

def main():
	
	while(True):
		
		cv2.imshow(windowName, rimage)
		
		k = cv2.waitKey(25)
		if k == 27:
			break
		# else:
		# 	print(k) enter = 13
		# elif k == 20:
		# 	pass
		# if k == ord('m') or k == ord('M'):

	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()