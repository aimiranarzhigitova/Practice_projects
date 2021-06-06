
from bs4 import BeautifulSoup
import requests


def save():
    with open('enter_parser.txt', 'a') as file:
        file.write(f"Цена : {comp['price']} Ссылка : {comp['link']}\n")

def parse():
    URL = 'https://enter.kg/computers/noutbuki_bishkek'
    HEADERS = {
        'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0'
    }

    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_='row')
    
    comps = []

    for item in items:
        comps.append({
            # 'title': item.find('span', class_='product_name').get_text(strip=True),
            'price': item.find('span', class_ = 'price').get_text(strip = True),
            'link' : URL + item.find('a').get('href')
        })

        global comp
        for comp in comps:
            print(f"Цена : {comp['price']} Ссылка : {comp['link']}\n")
            save()

    
    

parse()
