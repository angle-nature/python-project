import requests
from lxml import etree
import chaojiying

# 获取登录页面源码数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
}
url = 'http://www.chaojiying.com/user/login/'


# ***************************
# 创建Session会话  会自动保留Cookie值
session = requests.Session()
# **************************

page_text = session.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
img_src = 'http://www.chaojiying.com' + tree.xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img/@src')[0]

# 将验证码存储在本地
img_data = session.get(url=img_src, headers=headers).content
img_path = 'code.jpg'
with open(img_path, 'wb') as fp:
    fp.write(img_data)

# 调用打码平台的示例程序进行验证码图片数据识别
img_code = chaojiying.getCodeText(img_path, 1902)
print(img_code)

# 发起post请求，模拟登录
post_url = 'http://www.chaojiying.com/user/login/'

data = {
    'user': 'luomu2021',
    'pass': 'panzerjkl520',
    'imgtxt': img_code,
    'act': '1'
}
response = session.post(url=post_url, data=data, headers=headers)
print(response.status_code)
index_page_text = response.text

# 登录成功后的用户首页
with open('./chaojiying.html', 'w', encoding='utf-8') as fp:
    fp.write(index_page_text)

# 用户信息页面
userinfo_url = 'http://www.chaojiying.com/user/profile/'
# 必须用session会话发起请求，因为session携带了Cookie值，否则用requests请求后会止步在登录界面
userinfo_page_text = session.get(url=userinfo_url, headers=headers).text
with open('./userInfo.html', 'w', encoding='utf-8') as fp:
    fp.write(userinfo_page_text)
