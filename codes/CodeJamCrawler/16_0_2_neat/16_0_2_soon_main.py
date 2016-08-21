#!/usr/bin/env python3

import itertools
from scipy.stats import bernoulli


def create_test_case(n, l):
    return bin(n)[2:].zfill(l).replace('0', '-').replace('1', '+')


def invert_string(s):
    return ''.join(map(invert_symbol, s))


def brute_test_case(test_case, max_depth, depth=0):
    if depth == max_depth:
        return max_depth

    if all(x == '+' for x in test_case):
        return depth

    best_answer = max_depth
    for i in range(1, len(test_case) + 1):
        best_answer = min(best_answer,
                          brute_test_case(invert_string(test_case[:i]) + test_case[i:],
                                          best_answer, depth + 1))

    return best_answer


def invert_symbol(s):
    return '-' if s == '+' else '+'


def get_first_group(s):
    return ''.join(next(itertools.groupby(s))[1])


def invert_group(g):
    return invert_symbol(g[0]) * len(g)


def solve_test_case(s):
    first_group = get_first_group(s)
    turns_count = 0

    while len(first_group) != len(s):
        s = invert_group(first_group) + s[len(first_group):]
        first_group = get_first_group(s)
        turns_count += 1

    if all(x == '-' for x in s):
        turns_count += 1

    return turns_count


def solve_test_case_set(test_cases):
    return [solve_test_case(c) for c in test_cases]


def test_sample():
    test_cases = ['-', '-+', '+-', '+++', '--+-']
    expected = [1, 1, 2, 0, 3]
    answers = solve_test_case_set(test_cases)

    assert expected == answers, '{} != {}'.format(expected, answers)
    print('Sample tests passed')


def generate_test_case():
    d = bernoulli.rvs(0.5, size=100).astype('str')
    d[d == '1'] = '+'
    d[d == '0'] = '-'
    return ''.join(d)


def test():
    for i in range(2 ** 9):
        test_case = create_test_case(i, 9)
        answer = solve_test_case(test_case)
        brute_forced = brute_test_case(test_case, min(len(test_case), answer + 1))
        assert answer == brute_forced, \
            'Answer: {}, Brute forced: {}, Test: {}'.format(answer, brute_forced, test_case)
        print('Passed', test_case, 'test')
    print('All tests passed')


def main():
    # test_sample()
    # test()
    n = int(input())
    test_cases = [input() for _ in range(n)]
    for i, answer in enumerate(solve_test_case_set(test_cases), start=1):
        print('Case #{}: {}'.format(i, answer))


if __name__ == "__main__":
    main()
