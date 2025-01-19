from typing import Iterable
from numbers import Number

def mean(it: Iterable[Number]) -> float:
    """Calculate the mean of an iterable of numbers."""
    return sum(it) / len(it)

def std(it: Iterable[Number]) -> float:
    """Calculate the standard deviation of an iterable of numbers."""
    m = mean(it)
    squared_diffs = ((x - m) ** 2 for x in it)
    return (sum(squared_diffs) / len(it)) ** 0.5

