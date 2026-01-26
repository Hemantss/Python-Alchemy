"""
Python Alchemy

Module:
chapters.chapter_13_typing_smart.mini_project

A mini-project demonstrating the use of generics and type hints to create a data processing pipeline.
mypy will help ensure type safety across the different processing stages.
"""


from typing import Generic, TypeVar, List


# Define type variables for input and output types
T_in = TypeVar("T_in")
T_out = TypeVar("T_out")


# ------------------------------
# Generic Processor Base Class
# ------------------------------
class Processor(Generic[T_in, T_out]):
    """Base class for data processors using generics."""
    def process(self, data: T_in) -> T_out:
        raise NotImplementedError("Must implement process() in subclass.")
    

# ------------------------------
# Concrete Processor Implementations
# ------------------------------
class StringSplitter(Processor[str, List[str]]):
    """Splits a sentence string into a list of words."""
    def process(self, data: str) -> List[str]:
        words = data.split()
        print(f"StringSplitter Output: {words}")
        return words
    

class WordLengthConverter(Processor[List[str], List[int]]):
    """Converts list of words to list of their lengths."""
    def process(self, data: List[str]) -> List[int]:
        lengths = [len(word) for word in data]
        print(f"WordLengthConverter Output: {lengths}")
        return lengths
    

class AverageLengthCalculator(Processor[List[int], float]):
    """Computes the average word length."""
    def process(self, data: List[int]) -> float:
        if not data:
            return 0.0
        average = sum(data) / len(data)
        print(f"AverageLengthCalculator Output: {average}")
        return average
    

# ------------------------------
# Pipeline Executor
# ------------------------------
class Pipeline:
    """Chains multiple processors into a sequential pipeline."""
    def __init__(self):
        self.stages: List[Processor] = []

    def add_stage(self, processor: Processor) -> None:
        self.stages.append(processor)

    def run(self, data):
        """Passes data through each processor sequentially."""
        for stage in self.stages:
            data = stage.process(data)
        return data
    

# ------------------------------
# Example Usage
# ------------------------------
if __name__ == "__main__":
    # Create and configure pipeline
    pipeline = Pipeline()
    pipeline.add_stage(StringSplitter()) # str → List[str]
    pipeline.add_stage(WordLengthConverter()) # List[str] → List[int]
    pipeline.add_stage(AverageLengthCalculator())# List[int] → float
    sentence = "Type hints make Python safer and clearer"
    result = pipeline.run(sentence)
    print(f"\nFinal Result: Average word length = {result:.2f}")