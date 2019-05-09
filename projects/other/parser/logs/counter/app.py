import os
import urllib.parse
from urllib.parse import urlparse, parse_qs

logdir = 'log'

def list_log_dir(startpath):
	for dir, ch_dirs, ch_files in os.walk(startpath):
		if('counter' in dir):
			# print(dir)
			for filename in ch_files:
				load_file_parse(dir, filename)

def load_file_parse(dir, filename):
	fullname = os.path.join(dir, filename)
	print('{}{}'.format('\n', fullname))
	line_c = 0
	with open(fullname,'r') as f:
		for line in f.readlines():
			line_c = line_c + 1
			item = line.rstrip('\n')
			parsed_url = urllib.parse.urlparse('?' + item)
			q = urllib.parse.parse_qs(parsed_url.query)
			parse_request_item(q)
			# print('{}'.format(item))
	print('{}{}'.format('Lines:', line_c))

def parse_request_item(q):
	req = {}
	for k in q:
		req[k] = q[k][0]
	save_request_item(req)

def save_request_item(req):
	if('uid' in req):
		print(req['uid'])

if __name__ == '__main__':
	list_log_dir(logdir)


# def list_log_dir(startpath):
# 	for root, dirs, files in os.walk(startpath):
# 		level = root.replace(startpath, '').count(os.sep)
# 		indent = ' ' * 4 * (level)
# 		print('{}{}/'.format(indent, os.path.basename(root)))
# 		subindent = ' ' * 4 * (level + 1)
# 		for f in files:
# 			print('{}{}'.format(subindent, f))