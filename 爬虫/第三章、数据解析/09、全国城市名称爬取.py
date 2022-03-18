import requests
from lxml import etree

# 爬取页面源码数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
}
url = 'https://www.aqistudy.cn/historydata'
page_text = requests.get(url=url, headers=headers).text

# 数据解析
tree = etree.HTML(page_text)
# 存储的就是div标签对象 返回类型是列表
all_ul_list = tree.xpath('//div[@class="all"]/div[2]//li')

fp = open('allCity.txt', 'w', encoding='utf-8')

for ul in all_ul_list:
    # 局部解析
    # li_list = ul.xpath('./div[2]/li')
    # for li in li_list:
    city_name = ul.xpath('./a/text()')[0]
    fp.write(city_name + '\n')
    print(city_name, "写入成功！")