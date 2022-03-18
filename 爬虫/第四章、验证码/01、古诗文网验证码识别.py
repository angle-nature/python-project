import requests
from lxml import etree
import chaojiying
# 将验证码图片下载到本地

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
}
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
img_src = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]

# 将验证码存储在本地
img_data = requests.get(url=img_src, headers=headers).content
img_path = 'code.jpg'
with open(img_path, 'wb') as fp:
    fp.write(img_data)

# 调用打码平台的示例程序进行验证码图片数据识别
code = chaojiying.getCodeText(img_path, 1902)
print(code)