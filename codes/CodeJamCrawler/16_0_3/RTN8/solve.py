#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math


def optimal(from_, to_):
    if from_ % 2 == 0:
        yield from_
        from_ += 1
    for divider_candidate in range(from_, to_, 2):
        yield divider_candidate


def get_divider(x, from_, to_):
    for divider_candidate in optimal(from_, min(to_, int(math.sqrt(x)) + 1)):
        if x % divider_candidate == 0:
            return divider_candidate


def solve(n_and_j):
    n, j = n_and_j.split(' ')
    n, j = int(n), int(j)

    results_candidates = []
    results = []

    def generate_jamcoin_candidate():
        for bin_number in range(0, 2 ** (n - 1)):
            yield ('1{:0%sb}1' % (n - 2)).format(bin_number)

    jamcoin_candidate_generator = generate_jamcoin_candidate()

    def get_jamcoin_candidate(i):
        if i >= len(results_candidates):
            jamcoin_candidate = next(jamcoin_candidate_generator)
            results_candidates.append((
                jamcoin_candidate,
                {'nums': [int(jamcoin_candidate, b) for b in range(2, 11)],
                 'step': 2,
                 'results': [None] * 9}))
        return results_candidates[i]

    jamcoin_candidate_i = 0
    max_divider = 4
    max_jamcoin_i = 2
    max_bin_number = 2 ** (n - 1)

    while True:
        jamcoin_candidate, stats = get_jamcoin_candidate(jamcoin_candidate_i)
        all_done = True
        for i, num in enumerate(stats['nums']):
            if stats['results'][i]:
                continue
            divider = get_divider(num, stats['step'], max_divider)
            if divider:
                stats['results'][i] = divider
            else:
                all_done = False
        if all_done:
            results.append(jamcoin_candidate + ' ' + ' '.join(map(str, stats['results'])))
            results_candidates.pop(jamcoin_candidate_i)
            if len(results) == j:
                return '\n'.join(results)
        else:
            jamcoin_candidate_i += 1
        if jamcoin_candidate_i >= max_jamcoin_i:
            max_divider += 2
            jamcoin_candidate_i = 0
            max_jamcoin_i = min(max_bin_number, max_jamcoin_i * 2)


if __name__ == '__main__':
    cases_number = int(input())
    for case_number in range(1, cases_number + 1):
        input_args = input()
        print('Case #%s:\n%s' % (case_number, solve(input_args)))
