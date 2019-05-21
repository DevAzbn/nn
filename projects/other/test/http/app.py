
import json
import http.client

conn = http.client.HTTPSConnection('api.ipify.org', timeout = 10, check_hostname = False)

payload = '{}'
headers = {
	# 'authorization': "Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==",
	'content-type': "application/json",
	'accept': "application/json"
}

# path = path + "?"+ payload if reqType == "GET" and payload else path
conn.request('GET', '/?format=json', payload, headers)

res = conn.getresponse()
data = res.read()
conn.close()
data = data.decode('utf-8')
data = json.loads(data)

print(data['ip'])


# conn = http.client.HTTPSConnection('api.infobip.com')

# payload = '{\"from\":\"InfoSMS\",\"to\":\"41793026727\",\"text\":\"Test SMS.\"}'
# headers = {
# 	'authorization': "Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==",
# 	'content-type': "application/json",
# 	'accept': "application/json"
# }

# conn.request('POST', '/sms/1/text/single', payload, headers)