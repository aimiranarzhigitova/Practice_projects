
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

CSV = 'Enter_nout_hak.csv'
HOST = 'https://www.enter.kg/'
URL = 'https://enter.kg/computers/noutbuki_bishkek'
HEADERS = {
        'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0'
    }

def get_html(url, params=''):
    r = requests.get(url, headers = HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='row')
    
    comps = []

    for item in items:
        comps.append({
            'price': item.find('span', class_ = 'price').get_text(strip = True),
            'link' : URL + item.find('a').get('href')
        })

    return comps


def save(items, path):
    with open(path, 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow (['Цена','Ссылка'])
        for item in items:
            writer.writerow([item['price'], item['link']])

def parser():
    PAGENATION = input("Введите количество страниц: ")
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        comps = []
        for page in range(1, PAGENATION + 1):
            print(f'Страница №{page} готова')
            html = get_html(URL, params={'page' : page})
            comps.extend(get_content(html.text))
        save(comps, CSV)
        print('Парсинг готов')
        # print(news_list)
    else:
        print('Error')

            

parser()