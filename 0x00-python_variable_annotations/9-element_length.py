#!/usr/bin/env python3
"""
type an iterable object
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    type an iterable object
    """
    return [(i, len(i)) for i in lst]
