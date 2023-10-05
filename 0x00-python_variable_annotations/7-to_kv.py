#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    a type-annotated function that returns a tuple
    """
    return (k, float(v ** 2))
