import os
import sys

import numpy as np
import cv2
import json


args = sys.argv


params = ['--project=']


def main(d):
	
	prefix = './projects/'
	dpath = prefix + d

	cascade = cv2.CascadeClassifier(dpath + '/cascade/cascade.xml')

	files = os.listdir(dpath + '/test')
	files = filter(lambda x: x.endswith('.jpg') or x.endswith('.png'), files)

	for f in files:
		actfile = f
		filename = dpath + '/test/' + f
		print(filename)

		windowName = filename

		cv2.namedWindow(windowName)

		image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		# gray = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
		# gray = np.hstack((image, gray))

		# kernel = np.ones((5,5), np.float32) / 25
		# gray = cv2.filter2D(gray,-1,kernel)

		# image = cv2.medianBlur(image, 15)

		# image = cv2.bilateralFilter(image,9,75,75)

		# image = cv2.bitwise_not(image)
		# image = cv2.bitwise_and(image, gray)
		# img5 = cv2.bitwise_or(img1, img2)
		# img6 = cv2.bitwise_xor(img1, img2)

		items = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
		if len(items):
			for (x, y, w, h) in items:
				cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
		print(len(items))

		while(True):
			cv2.imshow(windowName, image)
			k = cv2.waitKey(25)
			if k == 13:
				break
			elif k == 27:
				sys.exit()
		
		cv2.destroyAllWindows()


if __name__ == "__main__":
	for a in args:
		if a.startswith(params[0]):
			dir = a[len(params[0]):]
			main(dir)