from typing import list, Union, Tuple, Dict
n : int = 5

name: str ="harry"

# List of integers
numbers: list[int] = [1, 2, 3, 4]

# Dictionary with string keys and integer values
user_ages: Dict[str, int] = {"Alice": 30, "Bob": 25}

# Tuple of specific types
coordinates: Tuple[float, float] = (40.7128, 74.0060)

def sum(a: int,b: int) -> int:
    return a+b 