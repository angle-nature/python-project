import requests

# UA：User-Agent(请求载体的身份标识符)
# UA检测：门户网站的服务器会检测对应请求的载体身份标识符，
#        如果检测到请求的载体身份标识符为某一款浏览器，说明该请求是一个正常的请求
#        否则不是一个正常的请求（即爬虫）,服务器很可能拒绝该请求

# UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
if __name__ == "__main__":
    # UA伪装：将对应的UA封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'
    }
    url = 'https://www.baidu.com/wd'
    # 处理url携带的参数：封装到字典中
    keyWord = input("enter a keyWord:")
    param = {'wd': keyWord}
    response = requests.get(url=url, params=param, headers=headers)
    # print(response.status_code)
    page_text = response.text
    # 持久化存储
    fileName = keyWord + ".html"
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
