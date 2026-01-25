"""
Python Alchemy

Module:
chapters.chapter_11_mastering_python_functions.mini_project_logging_profiling
Mini Project: Function Logging and Profiling with Decorators
-----------------------------------------------------------
This program demonstrates practical use of:
- Decorators for logging function calls
- Profiling function execution time
"""

import time
import functools
import logging

# Configure logging
logging.basicConfig(filename='.\\logs\\app_logs.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def log_function(func):
    """Decorator to log function calls."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Running function: {func.__name__} with arguments:{args} {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper


def profile_function(func):
    """Decorator to measure execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        logging.info(f"Function {func.__name__} executed in {elapsed:.4f} Seconds")
        return result
    return wrapper


# --- Real-world use case: Data processing ---
@profile_function
@log_function
def process_data(data):
    """Simulates a data processing task."""
    time.sleep(0.5) # simulate heavy computation
    return [item.upper() for item in data if len(item) > 3]


# Example execution
dataset = ["python", "ai", "decorator", "log"]
result = process_data(dataset)
print(result)