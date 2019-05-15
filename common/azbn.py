import os
import sys
import json
import time

# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../system')

class CreateAzbnCtrl(object):
	
	dir = None

	def __init__(self):
		"""Init function"""
		self.dir = os.path.dirname(os.path.abspath(__file__))
	
	def now(self):
		return time.time()
	
	def isWin(self):
		r = False
		if(os.name == 'nt'):
			r = True
		return r

	
	# def __call__(self, uid):
	# 	"""Get module for azbn"""
	# 	if uid in self._mdl:
	# 		return self._mdl[uid]
	# 	else:
	# 		return self

	# def __getitem__(self, uid):
	# 	"""Get item: azbn[]"""
	# 	if uid in self._data:
	# 		return self._data[uid]
	# 	else:
	# 		return None
	
	# def __setitem__(self, uid, value):
	# 	"""Set item: azbn[]"""
	# 	self._data[uid] = value

	# def loadJSON(self, uid = ''):
	# 	"""Load JSON from uid-file in common-dir"""
	# 	_path = os.path.dirname(os.path.abspath(__file__)) + '/../common/' + uid + '.json';
	# 	d = {}
	# 	with open(_path) as json_data:
	# 		d = json.load(json_data)
	# 	return d

azbn = CreateAzbnCtrl()
