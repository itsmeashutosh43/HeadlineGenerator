from bs4 import *
import urllib.request
import json,csv
import re

urlpg='https://onlinekhabr.onlinenetwork.com/category/24'
page = urllib.request.urlopen(urlpg)
soup = BeautifulSoup(page, 'html.parser')
pattern='https://onlinekhabar.onlinenetwork.com'
article = soup.find_all('div', attrs={'class': 'col-sm-3 part-ent'})
url=[]
for k in article:
    urls = list(set([a['href'] for a in k.findAll(name='a', href=True)]))
    url.append(urls)
article1=soup.find_all('div', attrs={'class': 'col-sm-9 detail-on'})
url1=[]
for k in article1:
    urls = list(set([a['href'] for a in k.findAll(name='a', href=True)]))
    url1.append(urls)
finalurl=[]
for k in url1:
    for j in k:
        finalurl.append(j)
for k in url:
    for j in k:
        finalurl.append(j)
for url in finalurl:
    if re.search(pattern,url):
        finalurl[finalurl.index(url)]=url
    else:
        finalurl[finalurl.index(url)]="https://onlinekhabar.onlinenetwork.com"+url
print(finalurl)
data={}
print(len(finalurl))
for url in finalurl:
    page1 = urllib.request.urlopen(url)
    soup1=BeautifulSoup(page1, 'html.parser')
    headings=soup1.find(name='div',attrs={'class': 'inner-section cover-news'})
    heading= [heading.get_text(strip=True)

                     for heading in headings.findAll('h1')]
    paragraphs = soup1.find(name='div', attrs={

            'class': 'tag news-content'})
    

    paragraph = [paragraph.get_text(strip=True)

                     for paragraph in paragraphs.findAll('p')]
    

    data["".join(heading)] = "".join(paragraph)
data_to_file= open( "C:/Users/Krishu Thapa/Desktop/__pycache__/onlinekhabar.csv",'w',encoding='utf-16')
csv_write=csv.writer(data_to_file)
for row1,row2 in data.items():
   csv_write.writerow([row1,row2])
