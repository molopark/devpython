# coding=utf-8
from bs4 import BeautifulSoup
import urllib.request
import re

with urllib.request.urlopen('http://www.krx.co.kr/main/main.jsp') as response:
    page = response.read()
    soup = BeautifulSoup(page, 'html.parser')
    # print(soup.prettify())
    index_info = soup.find_all('div', {'class', 'index-info'})
    # print(index_info)

    pattern_point = re.compile(r'\d{1,3}(?:,\d{3})*\.\d+')
    for index in index_info:
        name = index.find('span', {'class', 'index-name'})
        # print(name)
        price = index.find('span', {'class', 'index-price'})
        up = index.find('span', {'class', 'index-up'})
        down = index.find('span', {'class', 'index-down'})
        # up_down = up if (up != None) else down
        # print(f'{name.string:11}: {price.string:>9} {up_down.string}')
        is_up = (up is not None)
        up_down = up.string if is_up else down.string
        up_down_sign = '+' if is_up else '-'

        index_data = pattern_point.findall(up_down)
        print(f'{name.string:11}: {price.string:>9} {up_down_sign}{index_data[0]:>8} ({index_data[1]:>5}%)')
