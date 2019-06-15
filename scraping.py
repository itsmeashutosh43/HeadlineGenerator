import requests

import bs4

import pandas as pd

import json

import csv





def basicSoup(url):

    page = requests.get(url)

    soup = bs4.BeautifulSoup(page.content, 'html.parser')

    return soup





data = {}

session = requests.Session()
session.max_redirects=60

data_to_file = open("C:/Users/Krishu Thapa/Desktop/__pycache__/onlinekhb.csv",'w',encoding='utf-16')

csv_writer = csv.writer(data_to_file)

'''

This code only scrapes the technology news. Change myUrl to scrape other news as well.

'''

myUrl = "https://www.onlinekhabar.com/content/business/technology"



for i in range(1, 36):

    print("Doing page ", i)

    url = myUrl+'/page'+str(i)

    soup = basicSoup(url)



    allNews = soup.find(name='div', attrs={'class': 'list_child_wrp'})

    urls = list(set([a['href']

                     for a in allNews.findAll(name='a',attrs={'class': 'title__regular'},href=True)]))



    for url in urls:
        
        soup = basicSoup(url)

        heading = soup.find(name='h2', attrs={'class': 'mb-0'})

        heading = heading.get_text()



        paragraphs = soup.find(name='div', attrs={

            'class': 'ok__news--wrap'})



        paragraph = [paragraph.get_text(strip=True)

                     for paragraph in paragraphs.findAll('p')]


        data[heading] = paragraph


    for row1, row2 in data.items():

        csv_writer.writerow([row1, row2])
