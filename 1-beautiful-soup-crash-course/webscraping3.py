import requests
from lxml import html
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


url = 'https://groceries.aldi.ie/en-GB/drinks/Beer-Ciders?sortDirection=asc&page=1'

response = requests.get(url, headers=headers)
tree = html.fromstring(response.text)
data = tree.xpath('//div[@class="products-search-results"]/@data-context')

with open('test3.txt', 'w', encoding="utf-8") as f:
    f.write(str(data))

print(data)
product_name = json.loads(data[0])

# for each_product in product_name['SearchResults']:
#     print(each_product['FullDisplayName'])
