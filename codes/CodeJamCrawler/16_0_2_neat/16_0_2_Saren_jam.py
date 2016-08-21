#!/usr/bin/env python3
from time import time
from random import randint

FORMAT = "Case #{}: {}"

if __name__ == "__main__":
    cases = int(input())
    for i in range(cases):
        pancakes = [x == "+" for x in input()]
        flips = 0
        for j in range(len(pancakes) - 1, -1, -1):
            if not pancakes[j]:
                for k in range(0, j + 1):
                    pancakes[k] = not pancakes[k]
                flips += 1
        print(FORMAT.format(i + 1, flips))
