import urllib.request as ur
import urllib.parse as up
import json

# for manually input the url json_url = input("Enter the url >>> ")
json_url = "https://python-data.dr-chuk.net/comments_22962.json"  # url for the data(in json)

print('Retrieving ', json_url)
data = ur.urlopen(json_url).read().decode("utf-8")
print("Retrieved ", len(data),'characters')
json_obj = json.loads(data)

sum = 0
total_number = 0
for comment in json_obj["comments"]:
    sum +=  int(comment["count"])
    total_number += 1
print("Count ", total_number)
print("Sum : ", sum)
