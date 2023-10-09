#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    delays = []

    tasks = [wait_random(max_delay) for i in range(n)]

    results = await asyncio.gather(*tasks)

    delays = sorted(results)

    return delays
