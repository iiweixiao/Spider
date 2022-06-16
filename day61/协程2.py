import asyncio
import time


async def func1():
    print('func1 start')
    await asyncio.sleep(3)
    print('func1 end')

async def func2():
    print('func2 start')
    await asyncio.sleep(5)
    print('func2 end')

async def func3():
    print('func3 start')
    await asyncio.sleep(2.5)
    print('func3 end')

if __name__ == '__main__':
    start = time.time()
    tasks = [
        func1(),
        func2(),
        func3(),
    ]
    lop = asyncio.get_event_loop()
    lop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start)
