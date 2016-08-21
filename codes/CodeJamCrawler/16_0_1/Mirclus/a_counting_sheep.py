#! /usr/bin/env python3
import sys


def a_counting_sheep():
    test_cases = int(sys.stdin.readline())

    for test_case in range(test_cases):
        value = int(sys.stdin.readline())

        if value == 0:
            print("Case #{}: INSOMNIA".format(test_case + 1, value))
            continue

        missing = [str(i) for i in range(10)]

        number = 0
        while len(missing) > 0:
            number += value
            for c in [i for i in str(number)]:
                if c in missing:
                    missing.remove(c)

        print("Case #{}: {}".format(test_case + 1, number))


if __name__ == "__main__":
    a_counting_sheep()
