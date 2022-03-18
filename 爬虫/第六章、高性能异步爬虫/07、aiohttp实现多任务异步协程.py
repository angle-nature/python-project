import aiohttp
import asyncio
import time

urls = [
    # 'https://www.baidu.com',
    'https://www.sougou.com',
    'https://www.bilibili.com'
]

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67 '
}


async def request(url):
    await asyncio.sleep(2)
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url, headers=headers) as response:
            # text()返回字符串形式的响应数据
            # read()返回的二进制形式的响应数据
            # json()返回的就是json对象
            page_text = await response.text()
            # print(page_text)


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
