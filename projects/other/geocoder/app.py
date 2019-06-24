import sys
import json

import geocoder

if __name__ == '__main__':

	args = sys.argv

	params = ['--text=']

	for a in args:
		if a.startswith(params[0]):
			text = a[len(params[0]):]
			r = None
			try:
				res = geocoder.yandex(text)
				r = res.latlng
				r = (float(r[0]), float(r[1]))
			except:
				pass
			print(json.dumps(r))
			# print(res.city)
			# print(res.json)

			# g = geocoder.ip('199.7.157.0')
			# g = geocoder.ip('me')
			# print(g.latlng)
			# print(g.city)
