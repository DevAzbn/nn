import socket
import threading
from datetime import datetime

def scan_port(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.5)
	try:
		connect = sock.connect((ip, port))
		print('Port {} is open'.format(port))
		connect.close()
	except:
		pass

ip = '192.168.0.1'

start = datetime.now()
for i in range(1000):
	# scan_port(ip, i)
	th = threading.Thread(target = scan_port, args = (ip,i))
	th.start()
ends = datetime.now()
print('Time : {}'.format(ends - start))