#!/usr/bin/env python3

import itertools


def solve_test_case(n):
    seen_digits = set()

    if n == 0:
        return 'INSOMNIA'

    for x in itertools.count(1):
        new_value = n * x

        seen_digits = seen_digits.union(set(str(new_value)))
        if len(seen_digits) == 10:
            return new_value


def solve_test_case_set(test_cases):
    return [solve_test_case(c) for c in test_cases]


def test_sample():
    test_cases = [0, 1, 2, 11, 1692]
    expected = ['INSOMNIA', 10, 90, 110, 5076]

    assert expected == solve_test_case_set(test_cases)


def test_all_n():
    solve_test_case_set(range(0, 10 ** 6 + 1))


def main():
    # test_sample()
    # test_all_n()
    n = int(input())
    test_cases = [int(input()) for _ in range(n)]
    for i, answer in enumerate(solve_test_case_set(test_cases), start=1):
        print('Case #{}: {}'.format(i, answer))


if __name__ == "__main__":
    main()
