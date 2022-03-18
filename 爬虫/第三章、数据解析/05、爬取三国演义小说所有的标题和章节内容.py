import requests
from bs4 import BeautifulSoup
# 对首页的页面数据进行爬取
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
}
url = 'http://sanguo.5000yan.com/'
page_text = requests.get(url=url, headers=headers).content

# 在首页中解析出章节的标题和详情页的url
# 1、实例化BeautifulSoup对象、需要将页面源码数据加载到该对象中
soup = BeautifulSoup(page_text, 'lxml')
# 解析章节标题和详情页的url
li_list = soup.select('.sidamingzhu-list-mulu > ul > li')
fp = open('./sanguo.txt', 'w', encoding='utf-8')
for li in li_list:
    title = li.a.string
    detail_url = li.a['href']
    # 对详情页发出请求，解析出章节内容
    detail_page_text = requests.get(url=detail_url, headers=headers).content
    # 解析出详情页中相关的章节内容
    detail_soup = BeautifulSoup(detail_page_text, 'lxml')
    content = detail_soup.find('div', class_='grap').text

    # 存储在文本文件中
    fp.write(title+':'+content+'\n')
    print(title+',爬取成功!')
