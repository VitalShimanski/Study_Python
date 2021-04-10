#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://cars.av.by/renault"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'accept': '*/*'}
HOST = 'https://cars.av.by'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params = params)
    return r

def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div', class_='listing-item__wrap')
    cars = []
    for item in items:
        cars.append({
            'title': item.find('h3', class_='listing-item__title').get_text(strip=True),
            'link': HOST + item.find('a', class_='listing-item__link').get('href'),
            'price_BYN': item.find('div', class_='listing-item__price').get_text().replace('\u2009', ''),
            'price_usd': item.find('div', class_='listing-item__priceusd').get_text().replace('\u2009', ''),
            'location': item.find('div', class_='listing-item__location').get_text(strip=True),
            'date': item.find('div', class_='listing-item__date').get_text(strip=True),

        })
    print(cars)
    print(len(cars))

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()