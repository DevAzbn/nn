import os
import sys
import subprocess as sbp

sys.path.append( os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'common') )

from azbn import azbn
from db.mysql import connection

# print(azbn.isWin())
# print(azbn.now())
# print(azbn.dir)

if __name__ == '__main__':
	
	python = 'python3'
	if(azbn.isWin()):
		python = 'python'

	for dir, ch_dirs, ch_files in os.walk(azbn.dir):
		for filename in ch_files:
			if(filename.endswith('.py')):
				fullname = os.path.join(dir, filename)
				# print(fullname)
				res = str(sbp.run(python + ' ' + fullname, shell = True, stdout = sbp.PIPE).stdout, encoding='utf-8')
				# print(res)
				# pkgs = eval(str(sbp.run('pip3 list -o --format=json', shell = True, stdout = sbp.PIPE).stdout, encoding='utf-8'))
