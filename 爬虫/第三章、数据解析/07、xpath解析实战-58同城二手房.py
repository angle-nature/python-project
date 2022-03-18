import requests
from lxml import etree

# 爬取页面源码数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
}
url = 'https://wh.58.com/ershoufang/?utm_source=sem-360-pc'
page_text = requests.get(url=url, headers=headers).text

# 数据解析
tree = etree.HTML(page_text)
# 存储的就是div标签对象 返回类型是列表
div_list = tree.xpath('//section[@class="list"]/div')
# print(div_list)

fp = open('58.txt', 'w', encoding='utf-8')

for div in div_list:
    # 局部解析
    title = div.xpath('./a/div[2]/div[1]/div[1]/h3/text()')[0]
    fp.write(title+'\n')
    print(title+"：爬取成功！")
