import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter location: ')
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
parms = dict()
parms['address'] = address
parms['key'] = 42
#when you visit "http://py4e-data.dr-chuck.net/json?address=South%20Federal%20University" ,the broswer will tell u why need parameter "key"
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)

data = urllib.request.urlopen(url)
info = data.read().decode() # read data and decode
js = json.loads(info) # make for json format
print('Retrieved', len(info),'characters')  #test data is 3928 ,but this result of running is 2015
print('Place id',js['results'][0]['place_id'])
# print('Place id',js['results']['place_id']) is wrong beacuse "list indices must be integers or slices, not str"
