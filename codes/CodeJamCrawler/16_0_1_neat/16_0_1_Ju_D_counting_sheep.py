#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from collections import namedtuple
import logging
import sys
import time

CaseArgs = namedtuple('CaseArgs', ['n'])


def parse_cases(fin):
    case_count = int(fin.readline())
    for _ in range(case_count):
        n = int(fin.readline().strip())
        yield CaseArgs(n)


def command(options):
    cases_args = list(parse_cases(sys.stdin))
    case_count = len(cases_args)
    run_start_t = time.time()
    for idx, case_args in enumerate(cases_args):
        start_t = time.time()
        solution = solve(**case_args._asdict())
        print("Case #{num}: {solution}".format(
            num=idx+1,
            solution=solution
        ))
        end_t = time.time()
        logging.info("Case {num} of {total} solved in {t:.4f} seconds.".format(
            num=idx+1,
            total=case_count,
            t=end_t - start_t,
        ))
        logging.info("{:.2f} seconds elapsed.".format(
            end_t - run_start_t
        ))


def solve(n):
    fini = set(range(10))
    digits_seen = set()

    if n == 0:
        return 'INSOMNIA'

    for i in range(1, 5000 ):
        digits = set(int(c) for c in str(i * n))
        digits_seen |= digits
        logging.debug("{} * {} = {}".format(i, n, i * n))
        if digits_seen == fini:
            return n * i

    return 'INSOMNIA'


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
    sys.exit(main())
