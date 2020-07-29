from gevent import monkey
monkey.patch_all()
import gevent
import time
def down():
    print('爬虫开始')
    time.sleep(2)
    print('爬取结束')
t1 = time.time()
g_list=[]
for i in range(5):
    g = gevent.spawn(down)
    g_list.append(g)
gevent.joinall(g_list)
t2=time.time()
print(f'一共花费时间为{t2-t1}')

# import asyncio
# import aiohttp
# async def down(url):
#     async with aiohttp.ClientSession as session:
#         async with await session.get(url=url) as response:
#             page_text =await response.text()
#             print(page_text)











































