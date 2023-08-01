import asyncio

from background_work import test


async def background_main():
    asyncio.create_task(test.do_http_request())
