
class ImportEntity(object):
	
	# _row = None
	# _region_code = None
	# _parent = None
	# title = None
	# uid = None
	# parent_uid = None

	def __init__(self, row):
		"""Init function"""
		self._row = row
		self._region_code = None
		self._parent = None
		self.title = row.formalname.strip()
		self.uid = row.aoguid.strip()
		self.parent_uid = row.parentguid.strip()
	
	def regionCode(self, code = None):
		if(code != None):
			self._region_code = int(code)
		return self._region_code
	
	def parentObject(self, p = None):
		if(p != None):
			self._parent = p
		return self._parent
	
	def to_dict(self):
		res = {}
		return res

class ImportAdr(ImportEntity):
	
	# is_arch = None
	# prefix = None
	# code = None
	# cadnum = None
	# normdoc = None
	# postalcode = None
	# # plaincode = None
	# level = None
	# type = None
	# buildings = {}

	def __init__(self, row):
		"""Init function"""
		self._row = row
		self._region_code = None
		self._parent = None
		self.title = row.formalname.strip()
		self.uid = row.aoguid.strip()
		self.parent_uid = row.parentguid.strip()
		self.code = row.code.strip()
		self.prefix = row.shortname.strip()
		self.cadnum = row.cadnum.strip()
		self.normdoc = row.normdoc.strip()
		self.postalcode = row.postalcode.strip()
		self.level = None
		self.type = None
		self.buildings = {}
		self.level = row.aolevel
		if(row.actstatus):
			self.is_arch = 1
		else:
			self.is_arch = 0
		# self.plaincode = row.plaincode.strip()
		# 1 – уровень региона
		# 2 – уровень автономного округа
		# 3 – уровень района
		# 4 – уровень города
		# 5 – уровень внутригородской территории
		# 6 – уровень населенного пункта
		# 7 – уровень улицы
		# 90 – уровень дополнительных территорий
		# 91 – уровень подчиненных дополнительным территориям объектов
	
	def addBuilding(self, b):
		b_num = (
			b.housenum.strip().lower(),
			b.buildnum.strip().lower(),
			b.strucnum.strip().lower(),
		)
		b_num_stran_num = 0
		for m in b_num:
			if(len(m) > 0):
				b_num_stran_num = b_num_stran_num + 1
		b_num_str = ' '.join(b_num)
		b_num_str = b_num_str.strip().lower()
		if(b_num_str not in self.buildings):
			bld = {}
			bld['title'] = b_num_str
			bld['uid'] = b.houseguid.strip()
			bld['st'] = b.strstatus
			bld['nums'] = b_num
			# bld['parent'] = b.aoguid.strip()
			# if(b_num_stran_num > 1):
			# 	bld['st_num'] = 1
			# 	print('{}, {}, {}, {}'.format(self.title, '-'.join(bld['nums']), bld['status'], self.uid))
			# else:
			# 	bld['st_num'] = 0
			self.buildings[b_num_str] = bld
	
	def to_dict(self):
		res = {}
		res['title'] = self.title
		res['uid'] = self.uid
		if(self._parent):
			res['parent_uid'] = self._parent.uid
		else:
			res['parent_uid'] = None
		# res['region'] = {
		# 	'code' : self._region_code,
		# }
		res['level'] = self.level
		res['buildings'] = self.buildings
		return res
	
	def treePathTitle(self):
		res = ''
		res_arr = []
		# if(self._region_code):
		# 	res_arr.append(str(self._region_code))
		if(self._parent):
			res_arr.append(self._parent.treePathTitle())
		# res_arr.append(self.uid)
		res_arr.append(self.title)
		res = '/'.join(res_arr)
		return res
	
	def treePathUid(self):
		res = ''
		res_arr = []
		# if(self._region_code):
		# 	res_arr.append(str(self._region_code))
		if(self._parent):
			res_arr.append(self._parent.treePathUid())
		res_arr.append(self.uid)
		res = '/'.join(res_arr)
		return res


