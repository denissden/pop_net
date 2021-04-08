from typing import Callable
from apscheduler.schedulers.background import BackgroundScheduler
import time
import asyncio, concurrent.futures
from dataclasses import *


QUEUE_TICK = {"hours": 0, "minutes": 0, "seconds": 1}
POOL = concurrent.futures.ThreadPoolExecutor()


@dataclass(unsafe_hash=True)
class Process:
    name: field(default=str, hash=True)
    func: callable = field(hash=False, default=lambda: None)
    do_every: 1 = field(hash=False, default=lambda: 1)
    did_run: False = field(hash=False, default=lambda: False)
    next_start: 0 = field(default=lambda: time.time(), hash=False)

    def run(self):
        self.did_run = True
        self.func()