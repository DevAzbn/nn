import os
import json
import pickle

import dbf

def parse_table(reg_uid = 0, reg_crm_id = 0, file = '', row_num = 0):
	print('{}({}): {}'.format(reg_uid, reg_crm_id, file))

	table = dbf.Table(filename = file)
	table.open()
	# print(table[row_num])
	# for row in table:
	for i in range(row_num):
		print(table[i])
	table.close()


if __name__ == '__main__':
	# https://habr.com/ru/post/333424/
	src = {
		'dir' : '/home/azbn/www/tmp/fias/dbf',
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

		socr_file = '{}/{}{}.{}'.format(src['dir'], src['files']['socr'], '', src['ext'])
		parse_table(reg_uid, crm_id, socr_file, 1)
