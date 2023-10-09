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
    # Create a list to store the delays
    delays = []

    # Create a list of asyncio tasks for wait_random
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Execute all tasks concurrently using asyncio.gather
    results = await asyncio.gather(*tasks)

    # Sort the results in ascending order
    delays = sorted(results)

    return delays


async def main():
    n = 5
    max_delay = 10

    delays = await wait_n(n, max_delay)

    print("Delays in ascending order:")
    for delay in delays:
        print(f"{delay:.2f} seconds")
