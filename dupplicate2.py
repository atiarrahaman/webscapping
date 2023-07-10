import requests
from bs4 import BeautifulSoup

url='https://mybangla24.com/'
r=requests.get(url)
res=r.content
soup=BeautifulSoup(res,'html.parser')
box=set()
linkFind=soup.find_all('a')
for link in linkFind:
    if link.get('href') !='#':
       link_Text="https://mybangla24.com/" +link.get('href')
       box.add(link)
       print(link_Text)