import requests
import asyncio
import time

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67 '
}

urls = [
    # 'https://www.baidu.com',
    'https://www.sougou.com',
    'https://www.bilibili.com'
]


async def request(url):
    print("正在下载：", url)
    await asyncio.sleep(2)
    # request.get是基于同步，必须使用基于异步的网络请求模块进行指定url的请求发送
    # aiohttp:基于异步网络请求的模块
    # response = requests.get(url, headers)
    print("下载完毕！")


start = time.time()

# 任务列表
tasks = []

for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
# 需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(tasks))

print(time.time() - start)
