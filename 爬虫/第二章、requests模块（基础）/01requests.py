import requests
if __name__ =="__main__":  # 如果文件是主程序则执行
    # 指定url
    url = "https://www.sogou.com"
    # 发起请求  get方法会返回一个响应对象
    response = requests.get(url)
    # 获取响应数据 text返回的是字符串形式的响应数据
    page_text = response.text
    # 持久化存储
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)