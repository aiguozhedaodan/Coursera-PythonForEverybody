#Shibo: Written by python3, if it helps you, please click on "star"

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
incycle = input('Please enter the times for repeating process')
position = input('Please enter the position')
cycle = int(incycle)
n = int(position)
print("Retrieving:",url)
while cycle > 0:
    cycle = cycle - 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        n = n - 1
        url = tag.get('href', None)
        if n == 0:
            print("Retrieving:",url)
            n = int(position)
            break
