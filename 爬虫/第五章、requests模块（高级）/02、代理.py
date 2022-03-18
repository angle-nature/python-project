import requests

"""
代理：破解封IP这种反爬机制
什么是代理：
    - 代理服务器
代理的作用：
    - 突破自身IP访问的限制
    - 隐藏自身真实IP
代理相关的网站：
    - 快代理
    - 西祠代理
    - www.goubanjia.com
"""

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67 '
}
url = 'https://www.baidu.com/s?wd=ip'
# 处理url携带的参数：封装到字典中
response = requests.get(url=url, headers=headers, proxies={"https://": '104.129.202.19:8800'})
page_text = response.text
# 持久化存储
with open('ip.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
