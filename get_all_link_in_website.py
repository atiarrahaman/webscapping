import requests
from bs4 import BeautifulSoup


url="https://codewithharry.com/"

r=requests.get(url)
req=r.content
soup=BeautifulSoup(req,'html.parser')

res=soup.title

anchor=soup.find_all('a')
all_link=set()

for link in anchor:
    if link.get('href') !='#':
        link_text="https://codewithharry.com/" +link.get('href')
        all_link.add(link)
        print(link_text)


