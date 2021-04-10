#!/usr/bin/env python3
# fix #7 fixed code
import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://avto.abw.by/belarus/legkovye/prodazha/marka_citroen"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'accept': '*/*'}
HOST = 'https://avto.abw.by'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r
def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('div', class_='pages-wrapper')
    if pagination:
        return int(pagination[-1].get_text())
    return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='listing-item__wrap')
    print(items)

    cars = []
    for item in items:
        cars.append({
            'title': item.find('div', class_='b-item_title').get_text(),
            'link': HOST + item.find('a', class_='b-absolute_link').get('href'),
            'params': item.find('div', class_='listing-item__params').get_text().replace('\u2009', ''),
            'price_usd': item.find('div', class_='listing-item__priceusd').get_text().replace('\u2009', ''),
            'price_br': item.find('div', class_='listing-item__price').get_text().replace('\u2009', ''),
            'location': item.find('div', class_='listing-item__location').get_text(),


        })

    print(cars)



def parse():
    html = get_html(URL)
    cars = []
    pages_count = get_pages_count(html.text)
    if html.status_code != 200:
        print('Error')

    return
    for page in range(1, pages_count):
        print(f'Парсинг страницы {page} из {pages_count}...')
        html = get_html(URL, params={'page': page})
        cars.extend(get_content(html.text))
        #cars = get_content(html.text)
        #print(cars)


parse()



