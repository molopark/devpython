# coding=utf-8
import numpy as np
from typing import Dict


def main():
    a = np.arange(15)
    print(a)

    print(fib3(5))


memo: Dict[int, int] = {0: 0, 1: 1}


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]


if __name__ == "__main__":
    main()
