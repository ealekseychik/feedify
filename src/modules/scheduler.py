import asyncio
import logging

import uvloop

from src import vk_api_handler, tg_api_handler
from src.database.database import get_session
from src.conf.schedulerconfig import scheduler_delay_sec

logger = logging.getLogger(__name__)

class Scheduler:
    def __init__(self):
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        loop = asyncio.get_event_loop()
        loop.run_forever(_schedule_next())  # noqa: F821

    async def _schedule_next(self):
        while True:
            task_get_feed = asyncio.create_task(_get_feed())  # noqa: F821
            task_set_timer = asyncio.create_task(_set_timer())  # noqa: F821
            task_post_feed = asyncio.create_task(_post_feed())  # noqa: F821

            # Wait for tasks to complete
            await asyncio.gather(task_get_feed, task_set_timer, task_post_feed)

    async def _get_feed(self):
        pass

    async def _set_timer(self):
        await asyncio.sleep(scheduler_delay_sec)

    async def _post_feed(self):
        pass
