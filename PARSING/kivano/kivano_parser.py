
from bs4 import BeautifulSoup
import requests


def save():
    with open('kivano_parser.txt', 'a') as file:
        file.write(f"Ноутбук : {comp['title']}, Цена : {comp['price']} Ссылка : {comp['link']}\n")

def parse():
    URL = 'https://www.kivano.kg/noutbuki'
    HEADERS = {
        'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'
    }

    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_='item product_listbox oh')
    
    comps = []

    for item in items:
        comps.append({
            'title': item.find('div', class_ = 'listbox_title oh').get_text(strip = True),
            'price': item.find('div', class_ = 'listbox_price text-center').get_text(strip = True),
            'link' : URL + item.find('div', class_ = 'listbox_img pull-left').find('a').get('href')
        })

        global comp
        for comp in comps:
            print(f"Ноутбук : {comp['title']}, Цена : {comp['price']} Ссылка : {comp['link']}\n")
            save()

    
    

parse()

