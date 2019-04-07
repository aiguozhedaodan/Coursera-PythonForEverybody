import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving', url)
data = urllib.request.urlopen(url)
info = data.read().decode() # read data and decode
js = json.loads(info) # make for json format
print('Retrieved', len(info),'characters')  #sample is 2733 ,I DONT know where is the mistake

count = 0
value = 0
all = 0
for item in js['comments']:
    count = count + 1
    value = item['count']
    all = all + int(value)
print('Count:',count)
print('Sum:',all)
