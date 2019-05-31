class ImportEntity(object):
	
	_row = None
	_region_code = None
	_parent = None
	title = None
	uid = None
	parent_uid = None

	def __init__(self, row):
		"""Init function"""
		self._row = row
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
	
	def treePath(self):
		res = ''
		res_arr = []
		# if(self._region_code):
		# 	res_arr.append(str(self._region_code))
		if(self._parent):
			res_arr.append(self._parent.treePath())
		# res_arr.append(self.uid)
		res_arr.append(self.title)
		res = '/'.join(res_arr)
		return res
	
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

class ImportAdr(ImportEntity):
	
	is_arch = None
	prefix = None
	code = None
	cadnum = None
	normdoc = None
	postalcode = None
	# plaincode = None
	level = None
	type = None
	buildings = {}

	def __init__(self, row):
		"""Init function"""
		self._row = row
		self.title = row.formalname.strip()
		self.uid = row.aoguid.strip()
		self.parent_uid = row.parentguid.strip()
		self.code = row.code.strip()
		self.prefix = row.shortname.strip()
		self.cadnum = row.cadnum.strip()
		self.normdoc = row.normdoc.strip()
		self.postalcode = row.postalcode.strip()
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
		self.level = row.aolevel
		if(row.actstatus):
			self.is_arch = 1
		else:
			self.is_arch = 0
	
	def addBuilding(self, b):
		b_num = (
			b.housenum.strip(),
			b.buildnum.strip(),
			b.strucnum.strip(),
		)
		b_num_str = ''.join(b_num)
		if(b_num_str not in self.buildings):
			bld = {}
			bld['title'] = b_num_str
			bld['uid'] = b.houseguid.strip()
			bld['status'] = b.strstatus
			bld['nums'] = b_num
			bld['parent'] = b.aoguid.strip()
			self.buildings[b_num_str] = bld


class ImportBuilding(ImportEntity):
	
	def __init__(self, row):
		"""Init function"""
		self._row = row
		self.title = row.formalname.strip()
		self.uid = row.aoguid.strip()
		self.parent_uid = row.parentguid.strip()
		
