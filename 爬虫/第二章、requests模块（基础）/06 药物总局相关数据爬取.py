import requests
import json

if __name__ == "__main__":
    # UA伪装：将对应的UA封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
    }
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    id_List = [] # 存储企业的ID值
    all_data_list = [] # 存储所有企业的详情页
    # 参数的封装
    for page in range(1, 10):
        data = {
            'on': 'true',
            'page': '1',
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        # 请求发送 返回值为字典类型
        res_dict = requests.post(url=url, data=data, headers=headers).json()
        # 获取ID值
        for dic in res_dict['list']:
            id_List.append(dic['ID'])
        # print(id_List)

    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    # 参数的封装
    post_data = {
        'id': ''
    }
    for ID in id_List:
        post_data['id'] = ID
        detail_json = requests.post(url=post_url, data=post_data, headers=headers).json()
        all_data_list.append(detail_json)
        print(detail_json)

    # 持久化存储all_data_list
    fp = open('./allData.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)