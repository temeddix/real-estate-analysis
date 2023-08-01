import asyncio

import aiohttp


async def do_http_request():
    count = 1
    while True:
        print(f"YAHOO {count}")
        count += 1
        await asyncio.sleep(10)
