"""
Python Alchemy

Module:
chapters.chapter_13_typing_smart.generic_comparisons

Generic Comparisons Module
--------------------------------
This module demonstrates the use of generics and protocols to create
a function that compares two comparable objects.
mypy can enforce that only types supporting comparison operations
are used with the get_maximum function.
"""

from typing import TypeVar, Protocol

class Comparable(Protocol):
    def _lt_(self, other: object) -> bool: ...
    def _gt_(self, other: object) -> bool: ...

C = TypeVar("C", bound=Comparable)

def get_maximum(a: C, b: C) -> C:
    return a if a > b else b

print(get_maximum(10, 20)) # 20
print(get_maximum("cat", "dog")) # 'dog'
print(get_maximum([1], [2, 3])) # mypy: list is not Comparable