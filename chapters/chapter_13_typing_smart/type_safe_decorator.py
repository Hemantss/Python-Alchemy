
import time
from typing import Callable, TypeVar, ParamSpec

P = ParamSpec("P")
R = TypeVar("R")

def timed(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


@timed
def slow_add(a: int, b: int) -> int:
    time.sleep(1)
    return a + b


@timed
def greet(name: str) -> str:
    time.sleep(0.5)
    return f"Hello, {name}!"


slow_add(3, 7) # Type-safe, result: int
greet("Eve") # Type-safe, result: str