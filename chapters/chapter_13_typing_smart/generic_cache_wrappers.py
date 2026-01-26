"""
Python Alchemy

Module:
chapters.chapter_13_typing_smart.generic_cache_wrappers

Generic Cache Wrappers with Type Hints
--------------------------------
This module demonstrates the use of generics in type hints to create flexible cache wrappers.
mypy will help ensure type safety across different key-value types.
"""

from typing import TypeVar, Generic, Dict

K = TypeVar('K')
V = TypeVar('V')

class Cache(Generic[K, V]):
    def __init__(self):
        self._store: Dict[K, V] = {}

    def set(self, key: K, value: V) -> None:
        self._store[key] = value

    def get(self, key: K) -> V | None:
        return self._store.get(key)
    

cache = Cache[str, int]()
cache.set("user_id", 101)
print(cache.get("user_id")) # 101
cache.set("name", "Ivaan") # mypy: Incompatible type "str"; expected "int"