#!/usr/bin/python3

import os
import sys
import string
import random
import json
import codecs
import time

import keyword
#keyword.kwlist
#keyword.iskeyword(строка)


class AzbnConstructor(object):
	
	TITLE = 'Azbn App Engine for Python'
	VERSION = '0.1.2'
	IS_DEV = True
	
	def __init__(self):
		"""Init function"""
		self._mdl = {}
		self._data = {}
	
	def __call__(self, uid):
		"""Get module for azbn"""
		if uid in self._mdl:
			return self._mdl[uid]
		else:
			return self
	
	def load(self, uid, obj):
		"""Create module for azbn"""
		self._mdl[uid] = obj
		return self
	
	def __getitem__(self, uid):
		"""Get item: azbn[]"""
		if uid in self._data:
			return self._data[uid]
		else:
			return None
	
	def __setitem__(self, uid, value):
		"""Set item: azbn[]"""
		self._data[uid] = value
	
	def info(self):
		"""Echo TITLE and VERSION"""
		print(self.TITLE, self.VERSION)
	
	def echo(self, s):
		"""Echo string"""
		print(s)
		return self

	def now(self):
		"""Echo time()"""
		return time.time()

	def loadJSON(self, f = ''):
		"""Load JSON from uid-file in common-dir"""
		#_path = os.path.dirname(os.path.abspath(__file__)) + '/../common/' + uid + '.json';
		_path = f + '.json'
		d = {}
		with open(_path) as json_data:
			d = json.load(json_data)
		return d
	
	def saveJSON(self, f = '', o = None):
		_path = f + '.json'
		if o:
			with open(_path, 'w') as file:
				json.dump(o, file, ensure_ascii = False)
				#json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False)
				#indent=4, sort_keys=True
		pass
	
	def randstr(self, size=16, symbols = False):
		if symbols:
			spec = '!@#$%&*?^()-=_+.'
		else:
			spec = ''
		chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + spec
		#size = random.randint(8, 12)
		return ''.join(random.choice(chars) for x in range(size))
