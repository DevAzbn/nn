#!/usr/bin/python3

#pip install virtualenv
#pip install virtualenvwrapper
#pip install virtualenvwrapper-win
##pyassoc

#pip install SpeechRecognition
#pip install gTTS
#pip install PyAudio
#pip install pyttsx3
#pip install pypiwin32

import os
import sys

import azbn as azbnpy

arguments = sys.argv

azbn = azbnpy.AzbnConstructor()

#sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../system')

def main(argv):
	
	x = 2
	y = 3

	#print(azbn.randpart())
	#print(azbn.getMath().e)
	

	#print(3 ** 2)
	#if x < y:
	#	print(x)

	#if X:
	#	A = Y
	#else:
	#	A = Z
	#A = Y if X else Z

	#i = 5
	#while i < 15:
	#	print(i)
	#	i = i + 2

	#for i in 'hello world':
	#	print(i * 2, end='')

	#for i in 'hello world':
	#	if i == 'o':
	#		continue
	#	print(i * 2, end='')

	#for i in 'hello world':
	#	if i == 'o':
	#		break
	#	print(i * 2, end='')

	#for i in 'hello world':
	#	if i == 'a':
	#		break
	#else:
	#	print('Буквы a в строке нет')


	
	#with open('./hw2.txt', 'w') as f:
	#	try:
	#		f.write('Hello, World!')
	#	except Exception:
	#		print('Ошибка записи в файл')
	#	else:
	#		pass


	#f = open('./hw.txt', 'r')
	#try:
	#	str = f.read()
	#	print(str)
	#
	#	#days_file.readlines()
	#
	#	#with open("test.txt") as file_handler:
	#	#	for line in file_handler:
	#	# 		print(line)
	#
	#	#l = [line.strip() for line in f]
	#
	#except Exception:
	#	print('Ошибка чтения')
	#else:
	#	pass
	#finally:
	#	f.close()

	#l = 32
	#c = 32
	#for parameter in argv:
	#	if 'l=' in parameter:
	#		l = int(parameter[parameter.find('=')+1:])
	#	if 'c=' in parameter:
	#		c = int(parameter[parameter.find('=')+1:])
	##p = randompassword(l);
	#with open('passwords.txt', 'w') as f:
	#	for x in range(c):
	#		p = azbn.randstr(l)
	#		f.write(p)
	#		f.write('\n')

	#d = azbn.loadJSON('azbn')
	#azbn.saveJSON('azbn2', d)
	#print(d['dev'])

	#azbn.info()
	#azbn.echo(azbn.now())
	#azbn.echo(azbn.IS_DEV)

	pass

if __name__ == '__main__':
	main(arguments)
