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

	result = {}
	with open(dpath + '/marked.json') as json_data:
		result = json.load(json_data)

	str = ''
	for l in result:
		image = cv2.imread(dpath + '/pos/' + l, cv2.IMREAD_UNCHANGED)
		lcoord = ''
		for i in result[l]:
			if(i[1][0] > image.shape[1]):
				i[1][0] = image.shape[1]
			if(i[1][1] > image.shape[0]):
				i[1][1] = image.shape[0]
			lcoord = lcoord + " {} {} {} {}".format(i[0][0], i[0][1], i[1][0] - i[0][0], i[1][1] - i[0][1])
		str = str + "pos/{} {}{}".format(l, len(result[l]), lcoord) + "\n"
	with open(dpath + '/pos.txt', 'w') as fi:
		fi.write(str)


if __name__ == "__main__":
	for a in args:
		if a.startswith(params[0]):
			dir = a[len(params[0]):]
			main(dir)