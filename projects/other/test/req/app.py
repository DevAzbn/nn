import urllib.request
content = urllib.request.urlopen("https://ya.ru/").read()
print(content)