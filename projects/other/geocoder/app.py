import geocoder
res = geocoder.yandex('Орел, Грановского 2')
print(res.latlng)
print(res.city)
print(res.json)

# g = geocoder.ip('199.7.157.0')
# g = geocoder.ip('me')
# print(g.latlng)
# print(g.city)