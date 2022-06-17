import asyncio
import time


async def display(num):
    print('start')
    await asyncio.sleep(1)
    print(num)

s = time.time()
coroutines = [display(num) for num in range(10)]
# loop = asyncio.get_event_loop()
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(asyncio.wait(coroutines))
loop.close()
print(time.time()-s)
