import asyncio
import threading


async def start():
    while True:
        print("YAHOO")
        await asyncio.sleep(1)


threading.Thread(target=lambda: asyncio.run(start())).start()
