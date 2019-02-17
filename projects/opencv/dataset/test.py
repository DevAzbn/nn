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