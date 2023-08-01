import threading
import asyncio

from background_work import test


async def start():
    asyncio.create_task(test.do_http_request())


event_loop = asyncio.new_event_loop()
event_loop.create_task(start())
background_thread = threading.Thread(target=lambda: event_loop.run_forever())
background_thread.start()
