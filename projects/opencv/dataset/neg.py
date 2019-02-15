import os
import sys


args = sys.argv


params = ['--project=']


dpath = ''
result = []


def main(d):
	global dpath, result

	prefix = './projects/'
	dpath = prefix + d
	files = os.listdir(dpath + '/neg')
	files = filter(lambda x: x.endswith('.jpg') or x.endswith('.png'), files)

	for f in files:
		result.append(f)

		str = ''
		for l in result:
			str = str + "./neg/{}".format(l) + "\n"
		with open(dpath + '/neg.txt', 'w') as fi:
			fi.write(str)


if __name__ == "__main__":
	for a in args:
		if a.startswith(params[0]):
			dir = a[len(params[0]):]
			main(dir)