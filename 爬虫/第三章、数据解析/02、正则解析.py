import requests
import re
import os
# 需求：爬取糗事百科里热图板块里所有图片
url = 'https://www.qiushibaike.com/imgrank/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'
}
# 创建存放所有图片的文件夹
if not os.path.exists('./qiuTuLibs'):
    os.mkdir('./qiuTuLibs')

# 使用通用爬虫对url对应的一整张页面进行爬取
page_text = requests.get(url=url, headers=headers).text
# 使用聚焦爬虫将页面所有图片进行提取/解析 正则解析
ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
img_src_list = re.findall(ex, page_text, re.S)
# print(img_src_list)
for src in img_src_list:
    # 拼接出一个完整的图片url
    src = 'https:' + src
    # 请求到了图片的二进制数据
    img_data = requests.get(url=src, headers=headers).content
    # 生成图片名称
    img_name = src.split('/')[-1]
    # 图片路径
    imgPath = './qiuTuLibs/'+img_name
    with open(imgPath, 'wb') as fp:
        fp.write(img_data)
        print(img_name+" 写入成功")
