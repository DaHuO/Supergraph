#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from collections import namedtuple
import math
import logging
import sys
import time

CaseArgs = namedtuple('CaseArgs', ['n', 'j'])

JamCoin = namedtuple('JamCoin', ['coin', 'divisors'])


def parse_cases(fin):
    case_count = int(fin.readline())
    for _ in range(case_count):
        n, j = [int(cs) for cs in fin.readline().strip().split(' ')]
        yield CaseArgs(n, j)


def command(options):
    cases_args = list(parse_cases(sys.stdin))
    case_count = len(cases_args)
    run_start_t = time.time()
    for idx, case_args in enumerate(cases_args):
        start_t = time.time()
        solutions = solve(**case_args._asdict())
        print("Case #{num}:".format(
            num=idx+1,
        ))
        for solution in solutions:
            print(' '.join([solution.coin] + [str(d) for d in solution.divisors]))
        end_t = time.time()
        logging.info("Case {num} of {total} solved in {t:.4f} seconds.".format(
            num=idx+1,
            total=case_count,
            t=end_t - start_t,
        ))
        logging.info("{:.2f} seconds elapsed.".format(
            end_t - run_start_t
        ))


def solve(n, j):
    solutions = []

    cs = candidates(n)
    while len(solutions) < j:
        c = next(cs)
        logging.debug("Candidate: {}".format(c))
        divisors = is_coin_jam(c)
        if divisors:
            jc = JamCoin(c, divisors)
            logging.debug('Solution: {}'.format(jc))
            solutions.append(jc)

    return solutions


def is_coin_jam(c):
    divisors = []
    for val in candidate_values(c):
        divisor = get_divisor(val)
        if divisor:
            divisors.append(divisor)
        else:
            return False
    return divisors


def candidate_values(candidate):
    for i in range(2, 11):
        yield int(candidate, base=i)


def primes(maximum):
    store = []
    for i in range(2, maximum):
        for p in store:
            if i % p == 0:
                break
        else:
            store.append(i)
            yield i


small_primes = list(primes(200))


def get_divisor(num):
    num_root = math.sqrt(num)
    for p in (sp for sp in small_primes if sp < num_root):
        if num % p == 0:
            return p
    # TODO Not divisible by primes under 200, but that's okay, we can afford
    # a few false primes because we're throwing them away anyway.
    return None


def candidates(n):
    val = list((n - 2) * '0')
    idx = -1

    try:
        while True:
            val[idx] = '1' if val[idx] == '0' else '0'
            if val[idx] == '0':
                idx -= 1
            else:
                idx = -1
                yield '1' + ''.join(val) + '1'
    except IndexError:
        pass


def main(argv=sys.argv[1:]):
    try:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('-v', '--verbose', action='count', default=0)

        options = arg_parser.parse_args(argv)

        level = logging.WARNING
        if options.verbose == 1:
            level = logging.INFO
        elif options.verbose >= 2:
            level = logging.DEBUG
        logging.basicConfig(
            level=level,
            format="{levelname:>7s}: {message}",
            style="{",
        )

        command(options)
    except KeyboardInterrupt:
        pass

    return 0


if __name__ == '__main__':
    main()
