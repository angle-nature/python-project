import requests
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
}

data={
    'id': '26010',
    'classid': '66'
}

url = 'https://pic.netbian.com/downpic.php'
img_data = requests.get(url=url, params=data, headers=headers).content

with open('tupian.jpg', 'wb') as fp:
    fp.write(img_data)