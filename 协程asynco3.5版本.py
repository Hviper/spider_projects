'''python3.4官方推荐的方法： async & await 关键字代替了@asyncio.coroutine 和 yield from'''

import time
import asyncio



async def run1():
    print('执行代码一的上部分')
    #假如这里是一个网络 IO 请求
    await asyncio.sleep(2)
    print('执行代码一的下部分')


async def run2():
    print('执行代码二的上部分')
    # 假如这里是一个网络 IO 请求
    await asyncio.sleep(2)
    print('执行代码二的下部分')


start=time.time()
           # asyncio.Task(run1()) 和 asyncio.ensure_future(run1())
tasks=[asyncio.ensure_future(run1()),asyncio.ensure_future(run2())]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print('一共花费时间为:',time.time()-start)
