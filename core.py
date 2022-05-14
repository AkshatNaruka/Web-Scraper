from urllib.request import urlopen
from bs4 import BeautifulSoup
from google import search
import os

for url in search(ip, stop=):
     print(url)
htmldata = urlopen('https://www.geeksforgeeks.org/')
soup = BeautifulSoup(htmldata, 'html.parser')
images = soup.find_all('img')
  
for item in images:
    print(item['src'])