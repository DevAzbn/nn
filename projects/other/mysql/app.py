import os
import sys

import numpy as np
import pickle
import MySQLdb

# sudo apt-get install python-dev default-libmysqlclient-dev
# sudo apt-get install python3-dev

try:
	conn = MySQLdb.connect(host = '192.168.0.34', port = 3306, user = 'office_fedoperat', passwd = 'office_fedoperat', db = 'office_fedoperat', use_unicode = True, charset = 'utf8')
	cursor = conn.cursor(MySQLdb.cursors.DictCursor)
except MySQLdb.Error as err:
	print("Connection error: {}".format(err))

try:
	
	cursor.execute("""SELECT * FROM `external_ad` WHERE 1 ORDER BY RAND() LIMIT %s""", (3,))
	# .executemany
	# .query

	#rows = cursor.fetchmany(5)
	rows = cursor.fetchall()
	for item in rows:
		print(item['title'])

	# cursor.execute("SELECT * FROM `external_ad` WHERE 1 ORDER BY `id` LIMIT 20")

	# # Получаем данные.
	# row = cursor.fetchone()
	# print(row)

except MySQLdb.Error as err:
	print("Query error: {}".format(err))

# Разрываем подключение.
conn.close()
