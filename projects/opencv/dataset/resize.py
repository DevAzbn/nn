import os
import sys

import numpy as np
import cv2
import json


args = sys.argv

params = ['--project=']

def main(d):

	maxw = 800
	maxh = 600

	prefix = './projects/'
	dpath = prefix + d

	spaths = ['pos', 'neg']
	for _sp in spaths:
		print(_sp)

		files = os.listdir(dpath + '/' + _sp)
		files = filter(lambda x: x.endswith('.jpg') or x.endswith('.png'), files)

		for f in files:
			filename = dpath + '/' + _sp + '/' + f
			image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

			# scale_percent = 60 # percent of original size
			# width = int(img.shape[1] * scale_percent / 100)
			# height = int(img.shape[0] * scale_percent / 100)
			# dim = (width, height)

			if (image.shape[0] > maxh or image.shape[1] > maxw):
				print(image.shape)
				by_w = maxw / image.shape[1]
				by_h = maxh / image.shape[0]
				print(by_w, by_h)
				if (by_w < by_h):
					dim = (int(image.shape[1] * by_w), int(image.shape[0] * by_w))
				elif (by_w > by_h):
					dim = (int(image.shape[1] * by_h), int(image.shape[0] * by_h))
				else:
					dim = (int(image.shape[1] * by_w), int(image.shape[0] * by_w))
				# p = image.shape[0] / image.shape[1]
				print(dim)

				image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
				cv2.imwrite(filename, image)
				print(filename)


if __name__ == "__main__":
	for a in args:
		if a.startswith(params[0]):
			dir = a[len(params[0]):]
			main(dir)