import urllib.request,urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs

url = input("Enter the url >>> ")
html = urllib.request.urlopen(url).read()  #reading all html data
soup = bs(html,'html.parser')               #parsing html using bs4

tags = soup('a')			#finding & listing all anchor tags
for tag in tags:
	print(tag.get('href',None))
