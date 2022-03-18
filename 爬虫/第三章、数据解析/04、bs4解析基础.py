from bs4 import BeautifulSoup

# 将本地的html文档中的数据加载到该对象中
fp = open('./huazhuangping.html', 'r', encoding='utf-8')
soup = BeautifulSoup(fp, 'lxml')
# print(soup)

# soup.tagName返回的是html文件中第一次出现的tagName标签
# print(soup.meta)

# 第一种用法：find('tagName')等同于soup.tagName
# print(soup.find('meta'))
# 第二种用法：find('tagName', class_/id/其他属性='属性名') 属性定位
# print(soup.find('div', class_='dzpzmain'))

# find_all('tagName')返回所有tagName标签  返回值为一个列表
# 第二种用法：find_all('tagName', class_/id/其他属性='属性名') 属性定位
# print(soup.find_all('meta'))

# select('某种选择器(id,class,标签...)'),返回的是一个列表
# print(soup.select('meta'))
# 层级选择器使用方式 select('.hzbscin > div > div > span')，> 表示一个层级
# print(soup.select('.hzbscin > div > div > span')[0])
# 多层级选择器使用方式 select('.hzbscin > div span')，空格 表示多个层级
# print(soup.select('.hzbscin > div span')[0])

# 获取标签之间的文本数据：soup.title.text/string/get_text()
# text/get_text() 可以获取一个标签中所有的文本内容，可以跨层级
# string 只可以获取该标签下直系的文本内容
print(soup.find('div', class_='dzpzmain').text)
print(soup.find('title').string)
print(soup.find('div', class_='dzpzmain').string)
print(soup.find('title').get_text())

