import sys
import os
import csv
import urllib.request
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

###
# Example:
# sudo python ipinfo.py "https://ipinfo.io/AS62567" DigitalOcean
###

savePath = "/Users/user/Desktop/"
url = "https://ipinfo.io/AS62567"
name = "DigitalOcean"
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }

if len(sys.argv) == 3:
    url = sys.argv[1]
    name = sys.argv[2]
else:
    print("Enter url:")
    url = sys.stdin.readline()
    print("Enter name:")
    name = sys.stdin.readline().strip()

tmpName = "tmp.txt"
fileName = "ip-" + name + ".txt"
if os.path.exists(savePath + tmpName):
    os.remove(savePath + tmpName)
if os.path.exists(savePath + fileName):
    os.remove(savePath + fileName)

request = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(request).read()

# soup = BeautifulSoup(html, "html.parser")
soup = BeautifulSoup(html, "lxml")
data = soup.find_all("a")

f = open(savePath + tmpName, "a")
for i in data:
    if isinstance(i.string, str):
        f.write(i.string + "\n")
f.close()

command = "grep '/' " + savePath + tmpName + " | grep -v ':' > " + savePath + fileName
os.system(command)

os.remove(savePath + tmpName)
