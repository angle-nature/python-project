import requests
import json

if __name__ == "__main__":
    # UA伪装：将对应的UA封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
    }
    post_url = 'https://fanyi.baidu.com/sug'
    # post处理url携带的参数：封装到字典中
    keyWord = input("enter a keyWord")
    data = {'kw': keyWord}
    # 请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 获取响应数据 json方法返回的是一个对象(具体类型从网页中得知)
    # 只有确认了返回数据类型是json类的才可以用json方法
    dict_obj = response.json()
    print(dict_obj)
    # 持久化存储
    fileName = keyWord + ".json"
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dict_obj, fp=fp, ensure_ascii=False)
