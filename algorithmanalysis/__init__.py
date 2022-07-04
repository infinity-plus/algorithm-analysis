import time
import random
from enum import Enum
from typing import Callable


class CASES(Enum):
    BEST = 'BEST'
    WORST = 'WORST'
    AVERAGE = 'AVERAGE'


class Algorithm:
    @classmethod
    def get_random_list(cls, size: int) -> list[int]:
        return list(random.sample(range(size), size))

    @classmethod
    def analyze(cls, algorithm_func: Callable, case: Enum, size: int = 100):
        print(
            f"{case.name} case Runtime of the {algorithm_func.__name__} for:")
        small_input = Algorithm.get_random_list(size)
        if case == CASES.BEST:
            small_input.sort()
        if case == CASES.WORST:
            small_input.sort(reverse=True)
        try:
            start = time.time()
            inversions = algorithm_func(small_input)[1]
            end = time.time()
            print(f"\t{size} inputs: {end - start} seconds. {inversions=}")
        except RecursionError:
            print(f"\t{len(small_input)} inputs: RecursionError")