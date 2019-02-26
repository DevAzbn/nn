import os
import sys

import numpy as np
import pickle
import MySQLdb

# sudo apt-get install python-dev default-libmysqlclient-dev
# sudo apt-get install python3-dev

conn = MySQLdb.connect(host = '192.168.0.34', port = 3306, user = 'office_fedoperat', passwd = 'office_fedoperat', db = 'office_fedoperat', use_unicode = True, charset = 'utf8')
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

cursor.execute("""SELECT * FROM `external_ad` WHERE 1 ORDER BY `id` LIMIT %s""", (3,))
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

# Разрываем подключение.
conn.close()
