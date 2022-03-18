import requests
from lxml import etree
import os
# 爬取源码数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
}
url = 'https://pic.netbian.com/4kdongman/'
page_text = requests.get(url=url, headers=headers).text

# 解析数据 src的属性值  alt属性值
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slist"]//li')

if not os.path.exists('./picLibs'):
    os.mkdir('./picLibs')

for li in li_list:
    # 局部解析
    img4k_url = 'https://pic.netbian.com' + li.xpath('./a/@href')[0]
    img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
    # 通用处理中文乱码的解决方案
    img_name = img_name.encode('iso-8859-1').decode('gbk')
    # print(img_name, img4k_url)

    img_data_page_text = requests.get(url=img4k_url, headers=headers).text
    img_tree = etree.HTML(img_data_page_text)
    img4k_src = 'https://pic.netbian.com' + img_tree.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
    print(img4k_src)

    # 获取4k图片
    img_data = requests.get(url=img4k_src, headers=headers).content
    img_path = 'picLibs/' + img_name
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_name, "下载成功！")
