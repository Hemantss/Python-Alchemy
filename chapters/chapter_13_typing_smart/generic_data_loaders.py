"""
Python Alchemy

Module:
chapters.chapter_13_typing_smart.generic_data_loaders

Generic Data Loaders with Type Hints
--------------------------------
This module demonstrates the use of generics in type hints to create flexible data loaders.
mypy will help ensure type safety across different data types.
"""

from typing import TypeVar, Generic, Callable, List

T = TypeVar('T')
            
class DataLoader(Generic[T]):

    def __init__(self, source: Callable[[], List[T]]) -> None:
        self.source = source

    def load(self ) -> List[T]:
        return self.source()

# Example usage
def load_numbers() -> List[int]:
    return [1, 2, 3, 4]

def load_names() -> List[str]:
    return ["Eve", "Eva", "Evan"]

number_loader = DataLoader[int](load_numbers)
print(number_loader.load()) # List[int]

name_loader = DataLoader[str](load_names)
print(name_loader.load()) # List[str]