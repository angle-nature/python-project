import requests

# 如何爬取图片数据
url = 'https://img2.baidu.com/it/u=680795882,2417539503&fm=26&fmt=auto&gp=0.jpg'
# content返回的是二进制形式的图片数据
# text（字符串）    content（二进制）    json()（对象）
image_data = requests.get(url).content
with open('./qiutu.jpg', 'wb') as fp:
    fp.write(image_data)
