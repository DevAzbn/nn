import socket
import threading
from datetime import datetime

def scan_port(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.5)
	try:
		connect = sock.connect((ip, port))
		print('Port {} is open'.format(port))
		# result = sock.connect_ex((ip, port))
		# if result == 0:
		# 	print "Port {}: 	 Open".format(port)
		connect.close()
	except:
		pass
	# except KeyboardInterrupt:
	# 	print "You pressed Ctrl+C"
	# 	sys.exit()
	# except socket.gaierror:
	# 	print 'Hostname could not be resolved. Exiting'
	# 	sys.exit()
	# except socket.error:
	# 	print "Couldn't connect to server"
	# 	sys.exit()

ip = '192.168.0.1'

start = datetime.now()
for i in range(1000):
	# scan_port(ip, i)
	th = threading.Thread(target = scan_port, args = (ip,i))
	th.start()
ends = datetime.now()
print('Time : {}'.format(ends - start))