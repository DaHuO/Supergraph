#!/usr/bin/env python


def parse_test_cases():
    test_cases = []
    n_test_cases = int(input())
    for i in range(n_test_cases):
        test_case = int(input())
        test_cases.append(test_case)
    return test_cases


def get_last_number(n, mul=2):
    if n == 0:
        return
    digits = [False] * 10
    for c in str(n):
        digits[int(c)] = True
    while False in digits:
        val = n * mul
        mul += 1
        for c in str(val):
            digits[int(c)] = True
    return val


def solve():
    test_cases = parse_test_cases()
    for i, test_case in enumerate(test_cases):
        last_number = get_last_number(test_case)
        if last_number:
            print("Case #{}: {}").format(i+1, last_number)
        else:
            print("Case #{}: INSOMNIA").format(i+1)


if __name__ == '__main__':
    solve()
