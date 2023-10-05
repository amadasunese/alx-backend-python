#!/usr/bin/env python3
"""
Returns sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Complex types - mixed list
    """
    return float(sum(mxd_lst))
