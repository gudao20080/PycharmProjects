import queue
import time
import threading

q = queue.Queue()

# def add(f: int, to: int):
#     for i in range(f, to):
#         q.put(i)
#         time.sleep(1)
#
# threading._start_new_thread(add, (1, 100,))
# time.sleep(10)

# while True:
#     # value = q.get(True, 2)
#     try:
#         value = q.get_nowait()
#     except as f:
#         print(f)
#     print(value)


import asyncio
import functools


async def do_some_work(x):
    await asyncio.sleep(x)
    print('Waiting {}'.format(x))
    return 'Done after {}s'.format(x)


def callback(future):
    print('callback: ', future.result())
    return 'aa'


# def callback(t, future):
#     print('Callback:', t, future.result())

now = lambda: time.time()

start = now()


async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(3)

    tasks = [asyncio.ensure_future(coroutine1),
             asyncio.ensure_future(coroutine2),
             asyncio.ensure_future(coroutine3)]
    # task = loop.create_task(coroutine)
    # task = asyncio.ensure_future(coroutine)
    # task.add_done_callback(functools.partial(callback, 2))
    # print(task)
    # loop.run_until_complete(tasks)
    i = 0
    for task in tasks:
        i += 1
        task.add_done_callback(functools.partial(callable))

    done, pendings = await asyncio.wait(tasks)

    for task in tasks:
        print('Task ret: {}'.format(task.result()))

    print("main")



loop = asyncio.get_event_loop()

loop.run_until_complete(main())

# print('Task ret: {}'.format(task.result()))

print('TIME: {}'.format(now() - start))

import scrapy


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

from urllib import parse

j = parse.urljoin("http://www.baidu.com/dadhsd", '/100100')
print(j)
