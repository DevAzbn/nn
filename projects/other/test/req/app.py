import urllib.request

if __name__ == '__main__':
	content = urllib.request.urlopen("https://ya.ru/").read()
	print(content)