from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse, urllib.error
import ssl

count = 0
total = 0
i=0

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url_link = input("Enter the url here -->> ") Use ur custom link
url_link = ("http://py4e-data.dr-chuck.net/comments_22959.html")
html = urlopen(url_link, context= ctx).read()

soup = BeautifulSoup(html, "html.parser")

#getting all the anchor tags
tags = soup('span')
for tag in tags:
    count += 1
    print('\nItem : ',count)
    print("\nTAG : ",tag)
    print('Contents : ',tag.contents[0])
    print('Attrs :', tag.attrs)
    i = int(tag.contents[0])
    total = i+total
    print('Total is ',total)
