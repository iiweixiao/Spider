import asyncio


async def func():
    print('hihihi')


if __name__ == '__main__':
    coroutine = func()
    asyncio.run(coroutine)
