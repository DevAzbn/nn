import os
import sys
from random import randint

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

	spaths = ['pos']
	for _sp in spaths:
		print(_sp)

		files = os.listdir(dpath + '/' + _sp)
		files = filter(lambda x: x.endswith('.jpg') or x.endswith('.png'), files)

		i = 0

		for f in files:
			filename = dpath + '/' + _sp + '/' + f
			image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

			degr = randint(15, 45)

			rows = image.shape[0]
			cols = image.shape[1]

			M = cv2.getRotationMatrix2D((cols / 2, rows / 2), degr, 1)
			dst = cv2.warpAffine(image, M, (cols, rows))

			nname = dpath + '/' + _sp + '/rotate_' + str(i) + '.jpg'

			cv2.imwrite(nname, dst)
			i = i + 1
			print(nname)


if __name__ == "__main__":
	for a in args:
		if a.startswith(params[0]):
			dir = a[len(params[0]):]
			main(dir)