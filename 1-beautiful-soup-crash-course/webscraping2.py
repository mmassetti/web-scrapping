from bs4 import BeautifulSoup
import requests
from lxml import html
import json


import os
import requests


headers = {
    'authority': 'lottery1-intl.fwc22.tickets.fifa.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://lottery1-intl.fwc22.tickets.fifa.com/lottery/welcome_es.html',
    'accept-language': 'es-US,es-419;q=0.9,es;q=0.8,en;q=0.7',
}

response = requests.get(
    'https://lottery1-intl.fwc22.tickets.fifa.com/lottery/application_es.html#/step/selection/0/list', headers=headers).text

# soup = BeautifulSoup(response, 'lxml')

tree = html.fromstring(response)
data = tree.xpath('//div[@class="product-list-content"]/@data-context')
# product_name = json.loads(data[0])

print(data)

# Write content on a file
# with open('test1.txt', 'w', encoding="utf-8") as f:
#     f.write(str(individual_matches))

# print(individual_matches)
