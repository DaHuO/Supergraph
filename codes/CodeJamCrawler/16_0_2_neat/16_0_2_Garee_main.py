#!/usr/bin/env python3


def parse_test_cases():
    test_cases = []
    n_test_cases = int(input())
    for i in range(n_test_cases):
        test_case = input()
        test_cases.append(test_case)
    return test_cases


def flip(stack):
    stack = list(stack[::-1])
    for i, p in enumerate(stack):
        stack[i] = "-" if p == "+" else "+"
    return "".join(stack)


def get_idxs(stack):
    f_sad, l_sad,  f_happy = None, None, None
    for i, p in enumerate(stack):
        if p == "-":
            if f_sad is None:
                f_sad = i
            l_sad = i
        else:
            if f_happy is None:
                f_happy = i
    return f_sad, l_sad, f_happy


def count_min_flips(stack):
    flips = 0
    while "-" in stack:
        f_sad, l_sad, f_happy = get_idxs(stack)
        i = l_sad + 1
        if f_happy is not None and f_happy < f_sad:
            i = f_sad
        stack = flip(stack[:i]) + stack[i:]
        flips += 1
    return flips


def solve():
    test_cases = parse_test_cases()
    for i, test_case in enumerate(test_cases):
        min_flips = count_min_flips(test_case)
        print("Case #{}: {}".format(i + 1, min_flips))


if __name__ == '__main__':
    solve()
