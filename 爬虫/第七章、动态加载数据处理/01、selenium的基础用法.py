from selenium import webdriver
from lxml import etree

# 实例化一个浏览器对象（传入浏览器的驱动程序）
browser = webdriver.Edge(executable_path='./msedgedriver.exe')
# 让浏览器发起一个指定url对应请求
browser.get('http://scxk.nmpa.gov.cn:81/xk/')
# 获取浏览器当前页面的源码数据
page_text = browser.page_source

# 解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)

browser.quit()