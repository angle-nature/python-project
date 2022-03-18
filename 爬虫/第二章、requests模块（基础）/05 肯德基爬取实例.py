import requests
import json

if __name__ == "__main__":
    # UA伪装：将对应的UA封装到一个字典中
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'}
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    # post处理url携带的参数：封装到字典中
    keyWord = input("enter a keyWord")
    pI = input("enter a pageIndex")
    pS = input("enter a pageSize")
    data = {
        'cname': '',
        'pid': '',
        'keyword': keyWord,
        'pageIndex': pI,
        'pageSize': pS
    }
    # 请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 获取响应数据
    page_text = response.text
    print(page_text)
    # 持久化存储
    fileName = keyWord + ".json"
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(page_text, fp=fp, ensure_ascii=False)
