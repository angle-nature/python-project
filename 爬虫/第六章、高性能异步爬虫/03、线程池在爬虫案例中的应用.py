import random
import re
import requests
from lxml import etree
import os
from multiprocessing.dummy import Pool

# 需求：爬取梨视频的视频数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67 ',
}

# 原则：线程池处理的目的是阻塞且耗时的操作
# 对下述url发起请求解析出视频详情页的url和视频名称
url = 'https://www.pearvideo.com/category_59'
param = {
    'contId': '1738488',
    'mrd': '0.14107501066979733'
}

page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="categoryList"]/li')

# 存放所有视频的url 以及 name
video_list = []

for li in li_list:
    video_name = li.xpath('./div//div[@class="vervideo-title"]/text()')[0] + '.mp4'

    # 视频id 解密所需
    contID = str(li.xpath('./div/a/@href')[0]).split('_')[1]

    ajax_url = 'https://www.pearvideo.com/videoStatus.jsp?'
    params = {
        'contId': contID,
        'mrd': str(random.random())
    }

    # ajax请求头 加了'Referer': 'https://www.pearvideo.com/video_contID'后 才能正常访问得到所希望得到的结果
    ajax_headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3823.400 QQBrowser/10.7.4307.400',
        'Referer': 'https://www.pearvideo.com/video_' + contID
    }

    video_dic = requests.get(url=ajax_url, headers=ajax_headers, params=params).json()
    # 得到的是经过加密后的srcUrl地址
    video_srcUrl = video_dic["videoInfo"]['videos']["srcUrl"]

    # 此处视频地址做了加密即ajax中得到的地址需要加上cont-,并且修改一段数字为id才是真地址
    # 伪地址："https://video.pearvideo.com/mp4/third/20210810/1628757877653-11905134-100838-hd.mp4"
    # 真地址："https://video.pearvideo.com/mp4/third/20210810/cont-1738367-11905134-100838-hd.mp4"

    # 解密
    video_true_url = re.sub(r'\d{13}', 'cont-' + contID, video_srcUrl)

    # 添加到列表中
    video_dic = {
        'name': video_name,
        'url': video_true_url
    }
    video_list.append(video_dic)


# 创建存放视频的文件夹
if not os.path.exists('./video'):
    os.mkdir('./video')


def downloadVideo(videoDic):
    videoSrc = videoDic['url']
    videoName = videoDic['name']
    print("正在下载：" + videoName)
    video_data = requests.get(url=videoSrc, headers=headers).content
    with open('./video/' + videoName, 'wb') as fp:
        fp.write(video_data)
        print("下载完成：" + videoName)


# 实例化一个线程池对象
pool = Pool(9)
# 将列表中每一个列表元素传递给downloadVideo进行处理
pool.map(downloadVideo, video_list)

# 关闭线程池
pool.close()
pool.join()