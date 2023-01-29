import requests
import json
import aiohttp
import asyncio

# GET先URL
url = "http://localhost:8000/item/"

# JSON形式のデータ
json_data = {
    "name": "val1"
}


async def get_request(session, no):
    response = await session.get(f'http://localhost:8000/')
    content = await response.text()
    print(f"{time.strftime('%X')} - {response.status} {content}", end='')


async def main():
    tasks = []
    print(f"{time.strftime('%X')} - Start")
    async with aiohttp.ClientSession() as session:
        for n in range(3):
            tasks.append(get_request(session, n+1))
        await asyncio.gather(*tasks)
    print(f"{time.strftime('%X')} - Finish")

asyncio.run(main())
