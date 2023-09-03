# раннее были именовые кортежи или словари, а в модуле asyncio в event loop крутятся экземпляры классов Task
# Event loop:
#       coroutine > Task(Future)
import asyncio
from time import time


# @asyncio.coroutine
# def print_nums():
#     num = 1
#     while True:
#         print(num)
#         num += 1
#         yield from asyncio.sleep(1)
#
#
# @asyncio.coroutine
# def print_time():
#     count = 0
#     while True:
#         if count % 3 == 0:
#             print("{} seconds have passed".format(count))
#         count += 1
#         yield from asyncio.sleep(1)
#
#
# @asyncio.coroutine
# def main():
#     task_1 = asyncio.ensure_future(print_nums())
#     task_2 = asyncio.ensure_future(print_time())
#
#     yield from asyncio.gather(task_1, task_2)
# python 3.4 ^^^


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task_1 = asyncio.create_task(print_nums())
    task_2 = asyncio.create_task(print_time())

    await asyncio.gather(task_1, task_2)


if __name__ == '__main__':
    asyncio.run(main())
