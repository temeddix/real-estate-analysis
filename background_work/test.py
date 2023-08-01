import asyncio

import aiohttp


async def do_http_request():
    while True:
        print("YAHOO")
        await asyncio.sleep(10)
