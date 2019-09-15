import asyncio
import aiohttp


async def run():
    async with aiohttp.ClientSession() as session:
        return await session.get('http://127.0.0.1:8888/api/v1/login')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = []
    for _ in range(10):
        tasks.append(run())
    res = loop.run_until_complete(asyncio.gather(*tasks))
    print(res)
