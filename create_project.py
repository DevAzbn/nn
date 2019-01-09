import os
import sys

args = sys.argv

params = ['--path=']

for a in args:
	if a.startswith(params[0]):
		directory = a[len(params[0]):]
		if not os.path.exists(directory):
			try:
				os.makedirs(directory)
				with open(directory + '/.gitkeep', 'w') as f:
					f.write('')
			except Exception as e:
				print(e)
			else:
				pass
			finally:
				pass