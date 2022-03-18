import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67 ',
}

# 原则：线程池处理的目的是阻塞且耗时的操作
# 对下述url发起请求解析出视频详情页的url和视频名称
url = 'http://www.xinghuoboli.com/Static/Home/VideoJS/?Play=https://vod.hjbfq.com/20201219/YuULJVCT/index.m3u8'

page_text = requests.get(url=url, headers=headers).content
with open('av.m3u8', 'wb') as fp:
    print("正在下载...")
    fp.write(page_text)
