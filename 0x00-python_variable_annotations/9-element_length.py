#!/usr/bin/env python3
"""
A function’s tha return values with the appropriate types
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    A function’s tha return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
