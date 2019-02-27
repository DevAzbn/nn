import os
import sys
import json
from datetime import datetime

import numpy as np
import pickle
import MySQLdb

# sudo apt-get install python-dev default-libmysqlclient-dev
# sudo apt-get install python3-dev

cost_del = 100000

now = int(datetime.now().timestamp())
border_moment = now - (86400 * 30 * 3)
now_bm = now - border_moment

def nn__getAge(created_at = 0):
	global now, border_moment, now_bm
	res = 100 * (created_at - border_moment) / now_bm
	return res

def nn__getLevelPos(l = 1, ls = 1):
	return 100 * l / ls

def nn__getCost(c):
	global cost_del
	return c / cost_del

print(now)
print(datetime.fromtimestamp(now))

try:
	conn = MySQLdb.connect(host = '192.168.0.34', port = 3306, user = 'office_fedoperat', passwd = 'office_fedoperat', db = 'office_fedoperat', use_unicode = True, charset = 'utf8')
	cursor = conn.cursor(MySQLdb.cursors.DictCursor)
except MySQLdb.Error as err:
	print("Connection error: {}".format(err))

try:
	
	cursor.execute("""SELECT * FROM `external_ad` WHERE `adr` LIKE %s OR `adr` LIKE %s ORDER BY RAND() LIMIT %s""", ('%орел%', '%орёл%', 5,))
	# cursor.execute("""SELECT * FROM `external_ad` WHERE 1 ORDER BY RAND() LIMIT %s""", (5,))
	# .executemany
	# .query

	#rows = cursor.fetchmany(5)
	rows = cursor.fetchall()
	for item in rows:
		# print("{}, {}".format(datetime.fromtimestamp(item.get('created_at')), item.get('title')))
		
		item['data'] = json.loads(item.get('data'))

		# r = {}
		# r['age'] = 1 - (now - item.get('created_at'))

		# ((now - item.get('created_at')) / 86400)
		d = datetime.fromtimestamp(item.get('created_at'))
		age = nn__getAge(item.get('created_at'))
		level = nn__getLevelPos(item.get('level'), item.get('levels'))
		cost = nn__getCost(item.get('cost'))
		room_amount = item.get('room_amount')

		print("{}, {}, {}, {}, {}".format(d, age, level, cost, room_amount))

	# cursor.execute("SELECT * FROM `external_ad` WHERE 1 ORDER BY `id` LIMIT 20")

	# # Получаем данные.
	# row = cursor.fetchone()
	# print(row)

except MySQLdb.Error as err:
	print("Query error: {}".format(err))

# Разрываем подключение.
conn.close()
