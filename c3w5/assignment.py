import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
xml = urllib.request.urlopen(url, context=ctx)
data = xml.read() #If without this line, it will shows:TypeError: a bytes-like object is required, not 'HTTPResponse'
stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')
print('Count:', len(lst))

all = 0
for item in lst:
    value = item.find('count').text
    all = all + int(value)
print(all)
