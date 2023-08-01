import threading
import asyncio

from background_work.entry import background_main


event_loop = asyncio.new_event_loop()
event_loop.create_task(background_main())
background_thread = threading.Thread(target=lambda: event_loop.run_forever())
background_thread.start()
