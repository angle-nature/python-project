import requests
import json
if __name__ =="__main__":
    # UA伪装：将对应的UA封装到一个字典中
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'}
    post_url ='https://movie.douban.com/j/chart/top_list'
    # post处理url携带的参数：封装到字典中
    param = {
        'type': '24',
        'interval_id': '100:90',
        'diction': '',
        'start': '0',  # 从库中的第几部电影去取
        'limit': '20'  # 一次取出的个数
    }
    # 请求发送
    response = requests.get(url=post_url, params=param, headers=headers)
    # 获取响应数据 json方法返回的是一个对象
    # 只有确认了返回数据类型是json类的才可以用json方法
    list_obj = response.json()
    print(list_obj)
    # 持久化存储
    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(list_obj, fp=fp, ensure_ascii=False)
