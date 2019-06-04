import os
import json
import pickle

import dbf

from crmclasses import ImportAdr

adrs = {}
blds = {}

def parse_table(reg_uid = 0, reg_crm_id = 0, file = '', row_num = 0):
	print('{}({}): {}'.format(reg_uid, reg_crm_id, file))

	table = dbf.Table(filename = file)
	table.open()
	# print(table[row_num])
	for row in table:
		print(row)
	table.close()

def parse_adrs_table(reg_uid = 0, reg_crm_id = 0, file = ''):
	global adrs, blds
	print('{}({}): {}'.format(reg_uid, reg_crm_id, file))

	adrs = {}
	blds = {}
	
	table = dbf.Table(filename = file, codepage = 'cp866')
	count = 0
	table.open()
	for row in table:
		# if(row.aoguid == '56ea5590-333f-4f19-951b-0fd75fd08aee'):
		# 	if(row.actstatus):
		# 		print(row)
		if(row.actstatus):
			adr = ImportAdr(row)
			adr.regionCode(reg_uid)
			if(adr.uid not in adrs):
				adrs[adr.uid] = adr
				print('import {}'.format(adr.title))
	table.close()

	for adr_uid in adrs:
		adr = adrs[adr_uid]
		print('>', adr.title)
		if(adr.parent_uid != ''):
			if(adr.parent_uid in adrs):
				adr.parentObject(adrs[adr.parent_uid])
				print('parent {} {}'.format(adrs[adr.parent_uid].title, adr.title))


def parse_blds_table(reg_uid = 0, reg_crm_id = 0, file = ''):
	global adrs, blds
	print('{}({}): {}'.format(reg_uid, reg_crm_id, file))

	# adrs = {}
	blds = {}

	table = dbf.Table(filename = file, codepage = 'cp866')
	count = 0
	table.open()
	for row in table:
		count = count + 1
		if(row.aoguid in adrs):
			# print(adrs[row.aoguid].uid, row.aoguid)
			adr = adrs[row.aoguid]
			adr.addBuilding(row)
			# STRSTATUS — признак строения (от 0 до 4, где 0 — никакого, 1 — строение, 2 — сооружение, 3 — литера).
			print('h {}	b {}	s {}	g {}	st {}'.format(row.housenum.strip(), row.buildnum.strip(), row.strucnum.strip(), row.houseguid.strip(), row.strstatus))
		# if(row.aoguid == '56ea5590-333f-4f19-951b-0fd75fd08aee'):
			# bld = ImportBuilding(row)
			# bld.regionCode(reg_uid)
			# if(bld.uid not in blds):
			# 	blds[bld.uid] = bld
			# 	print(bld)
			# 	print('import {}'.format(bld.title))
	table.close()
	# print(count)

def save_adrs_table(reg_uid = 0, reg_crm_id = 0):
	global adrs

	for adr_uid in adrs:
		adr = adrs[adr_uid]
		tree_path = adr.treePathTitle()
		d = adr.to_dict()
		fdir = 'data/{}'.format(tree_path)
		fpath = '{}/item.json'.format(fdir)
		if(not os.path.exists(fdir)):
			os.makedirs(fdir, 0o755)
		with open(fpath, 'w') as file:
			json.dump(d, file, ensure_ascii = False)
			if(adr._parent):
				print('saving {} {}'.format(adr._parent.title, adr.title))
			else:
				print('saving {}'.format(adr.title))
	


if __name__ == '__main__':
	# https://habr.com/ru/post/333424/
	src = {
		# 'dir' : '/home/azbn/www/tmp/fias/dbf',
		'dir' : 'X:\\dev\\OSPanel\\domains\\crm.localhost\\var\\app\\cache\\adrs\\src',
		'ext' : 'DBF',
		'files' : {
			'adrs' : 'ADDROB',
			'blds' : 'HOUSE',
			'nrms' : 'NORDOC',
			'socr' : 'SOCRBASE',
		},
	}
	regions = {
		'57' : {
			'crm_id' : 50,
		},
		# '36' : {
		# 	'crm_id' : 14,
		# },
		# '23' : {
		# 	'crm_id' : 32,
		# },
		# '77' : {
		# 	'crm_id' : 41,
		# },
		# '78' : {
		# 	'crm_id' : 58,
		# },
	}
	for reg_uid in regions:
		
		reg = regions[reg_uid]
		crm_id = reg['crm_id']

		print('{}: {}'.format(reg_uid, reg['crm_id']))

		adrs_file = '{}/{}{}.{}'.format(src['dir'], src['files']['adrs'], reg_uid, src['ext'])
		blds_file = '{}/{}{}.{}'.format(src['dir'], src['files']['blds'], reg_uid, src['ext'])
		
		parse_adrs_table(reg_uid, crm_id, adrs_file)
		parse_blds_table(reg_uid, crm_id, blds_file)
		save_adrs_table(reg_uid, crm_id)




		# with open(adrs_file + '.pickle', 'wb') as handle:
		# 	pickle.dump(adrs, handle, protocol = pickle.HIGHEST_PROTOCOL)

		# socr_file = '{}/{}{}.{}'.format(src['dir'], src['files']['socr'], '', src['ext'])
		# parse_table(reg_uid, crm_id, socr_file, 0)

	
	# 			# 1 – уровень региона
	# 			# 2 – уровень автономного округа
	# 			# 3 – уровень района
	# 			# 4 – уровень города
	# 			# 5 – уровень внутригородской территории
	# 			# 6 – уровень населенного пункта
	# 			# 7 – уровень улицы
	# 			# 90 – уровень дополнительных территорий
	# 			# 91 – уровень подчиненных дополнительным территориям объектов

	# 			if(row.aolevel == 1 or row.aolevel == 4):
	# 				# PARENTGUID ID родительского элемента. При поиске города к которому принадлежит улица. PARENTGUID улицы будет совпадать с AOGUID улицы.
	# 				print((row.actstatus, row.aoguid, row.aoid, row.aolevel, row.centstatus, row.parentguid, row.postalcode, row.regioncode, row.formalname.strip(), row.offname.strip()))
	# 			# print row[0:3]
	# 			# print row['name':'qualified']
	# 			# print [row.name, row.age, row.birth]







	# for adr_uid in adrs:
	# 	adr = adrs[adr_uid]
	# 	tree_path = adr.treePath()
	# 	d = adr.to_dict()
	# 	fdir = 'data/{}/{}'.format(reg_uid, tree_path)
	# 	fpath = '{}/adr.json'.format(fdir)
	# 	if(not os.path.exists(fdir)):
	# 		os.makedirs(fdir, 0o755)
	# 	with open(fpath, 'w') as file:
	# 		json.dump(d, file, ensure_ascii = False)
	# 		if(adr._parent):
	# 			print('{} {}'.format(adr._parent.title, adr.title))
	# 		else:
	# 			print('{}'.format(adr.title))

			# # if(row.aoguid not in adrs):
			# # 	adrs[row.aoguid] = row.formalname.strip()
			# # else:
			# # 	print(adrs[row.aoguid])
			# _uid_ = row.aoguid.strip()
			# _parent_ = row.parentguid.strip()
			# if(_uid_ not in adrs):
			# 	adr = ImportAdr(row)
			# 	adr.regionCode(reg_uid)
			# 	if(_parent_ in adrs):
			# 		adr.parentObject(adrs[_parent_])
			# 	adrs[adr.uid] = adr
			# 	tree_path = adr.treePath()
			# 	d = adr.to_dict()
			# 	fdir = 'data/{}/{}'.format(reg_uid, tree_path)
			# 	fpath = '{}/data.json'.format(fdir)
			# 	if(not os.path.exists(fdir)):
			# 		os.makedirs(fdir, 0o755)
			# 	with open(fpath, 'w') as file:
			# 		json.dump(d, file, ensure_ascii = False)
			# 		if(adr._parent):
			# 			print('{} {}'.format(adr._parent.title, adr.title))
			# 		else:
			# 			print('{}'.format(adr.title))



			
			# if(row.aolevel == 1 or row.aolevel == 4):
			# 	# PARENTGUID ID родительского элемента. При поиске города к которому принадлежит улица. PARENTGUID улицы будет совпадать с AOGUID улицы.
			# 	print((row.actstatus, row.aoguid, row.aoid, row.aolevel, row.centstatus, row.parentguid, row.postalcode, row.regioncode, row.formalname.strip(), row.offname.strip()))
			# print row[0:3]
			# print row['name':'qualified']
			# print [row.name, row.age, row.birth]

	# print('count {}'.format(count))