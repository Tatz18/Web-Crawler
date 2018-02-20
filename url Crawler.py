from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse, urllib.error
import ssl



ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.varify_mode =ssl.CERT_NONE

def itteration(c,n):
    inner_count = 0   # It counts the internal itteration of the lines
    position = 0     # it counts the sequeces of the position
    for tag in tags:
        position += 1
        while position >= n:
            print(position , "Retrieving: ",tag.get('href',None))
            inner_count += 1
            break
        if inner_count==c:break
        

url_link = input("Enter The URL -->>")
counting = int(input("Enter The itteration time : "))
num_pos = int(input("Enter the position: "))     #from where the counting will start
web_file = urlopen(url_link, context = ctx).read()
soup = BeautifulSoup(web_file, 'html.parser')

tags = soup('a')
itteration(counting, num_pos)


