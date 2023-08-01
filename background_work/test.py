import asyncio

import aiohttp


async def do_http_request():
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get("http://python.org") as response:
                print("Status:", response.status)
                print("Content-type:", response.headers["content-type"])

                html = await response.text()
                print("Body:", html[:15], "...")
            await asyncio.sleep(30)
