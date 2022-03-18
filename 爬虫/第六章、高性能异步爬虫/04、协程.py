import asyncio


async def request(url):
    print("正在请求的url是：", url)
    print("请求成功！", url)
    return url


# async修饰的函数，调用之后会返回一个协程对象
c = request("www.baidu.com")

# 创建一个事件循环对象
loop = asyncio.get_event_loop()

# 将协程对象注册到loop中，然后启动loop
# loop.run_until_complete(c)

# task的使用
# task = loop.create_task(c)
# # task还未没被执行
# print(task)
# loop.run_until_complete(task)
# # task已被执行
# print(task)

# future的使用
# future = asyncio.ensure_future(c)
# print(future)
# loop.run_until_complete(future)
# print(future)


# 回调函数
def callback_func(task):
    print(task.result())


# 回调绑定
future = asyncio.ensure_future(c)
# 将回调函数绑定到任务对象中 默认将任务对象传递给回调函数的参数
future.add_done_callback(callback_func)
loop.run_until_complete(future)
