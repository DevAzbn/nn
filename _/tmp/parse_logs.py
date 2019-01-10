#!/usr/bin/env python3

import os
import sys
import re
from ftplib import FTP

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../../../system')

import azbn as azbnpy

azbn = azbnpy.CreateAzbn()
app = azbnpy.CreateApp()

ftp = FTP()

def check_alert(file, res):
	if 'is_post' in res:
		print(file, res['ip'], res['req'])

def parseLine(line):
	res = {};
	
	res_arr = line.split(' ')
	if res_arr[2] != '-':
		res['user'] = res_arr[2]
	
	regexp_ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
	ips = re.findall(regexp_ip, line)
	res['ip'] = ips[0]
	
	regexp_post = r'\s\"POST\s'
	is_post = len(re.findall(regexp_post, line))
	if is_post :
		res['is_post'] = True
		
		regexp_req = r'\s\"POST\s([\S]{1,})'
		res['req'] = re.findall(regexp_req, line)
		if len(res['req']) > 0:
			res['req'] = res['req'][0]
		else:
			res['req'] = None
	
	return res

#def listing(data):
#	regexp_file = r'\s(nginx-access-[\S\.-]{1,}\.log)'
#	for k in data.split('\n'):
#		filename = re.findall(regexp_file, k)
#		if len(filename) > 0:
#			print(filename[0])
#			out = './data/' + filename[0]
#			with open(out, 'wb') as f:
#				ftp.retrbinary('RETR ' + 'log/' + filename[0], f.write)
#				

def nlisting(data):
	regexp_file = r'nginx-access-'
	for k in data:
		is_finded = re.findall(regexp_file, k)
		if len(is_finded) > 0:
			print(k)
			out = './data/' + k
			with open(out, 'wb') as f:
				def w_callback(data):
					f.write(data)
				ftp.retrbinary('RETR ' + k, w_callback)
			with open(out, 'r') as f:
				for line in f.readlines():
					res = parseLine(line)
					check_alert(out, res)

def main():
	ftp.connect('server', 21)
	ftp.login('user', 'pass')
	ftp.cwd('log')
	nlisting(ftp.nlst())
	
	#ftp.dir('log', listing)
	
	#data = ftp.retrlines('LIST')
	#print(data)
	
	#with open('./logs.log', 'r') as f:
	#	for line in f.readlines():
	#		res = parseLine(line)
	#		if 'is_post' in res:
	#			print(res)

if __name__ == '__main__':
	main()