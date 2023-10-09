#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    The basics of async
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> float:
    delays = []

    tasks = [wait_random(max_delay) for _ in range(n)]

    results = await asyncio.gather(*tasks)

    delays = sorted(results)

    return delays
