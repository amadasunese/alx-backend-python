#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A type-annotated function that multiplies a float
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
