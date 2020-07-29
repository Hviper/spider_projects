'''await 和 yield from 表示当它们后面的代码为阻塞操作时主动挂起，不会对其进行等待，而是继续执行下面的代码 '''
import asyncio
async def run1():
    print('执行代码一的上部分')
    await asyncio.sleep(2)
    print('执行代码二的上部分')
    return 'http://www.baidu.com'
async def run2():
    print('执行代码一的上部分')
    await asyncio.sleep(2)
    print('执行代码二的上部分')

def callback_fun(task):
    print('这是run1()函数需要的回调函数，即为后续对run1函数的操作')
    #result返回的就是任务对象中封装的协程对象对应的返回值
    print(task.result())

loop = asyncio.get_event_loop()

task1 = asyncio.ensure_future(run1())        #对于这个task1假如它的后面还需要有其他代码的实现，则需要绑定回调函数,将回调函数的名称作为参数传进去
task1.add_done_callback(callback_fun)

task2 = asyncio.ensure_future(run2())


tasks=[task1,task2]    #任务列表要封装到这里面去asyncio.wait(tasks)
loop.run_until_complete(asyncio.wait(tasks))




