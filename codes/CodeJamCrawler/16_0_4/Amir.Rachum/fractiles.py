import os
import time

import math
import pytest
import itertools
import collections
from contextlib import contextmanager
from typing import List


INPUT_TYPE = 'small'


Case = collections.namedtuple('Case', ['k', 'c', 's'])


def solve(case: Case):
    """break 'case', solve and return the solution"""
    if case.s < case.k // case.c:
        return 'IMPOSSIBLE'

    position_coords = []
    current = 0
    while len(position_coords) < math.ceil(case.k / case.c):
        coord = []
        while len(coord) < case.c:
            coord += [current]
            current += 1
            current %= case.k
        position_coords += [coord]

    positions = []
    for coord in position_coords:
        position = 0
        for i in range(case.c):
            position += coord[i] * case.k ** (case.c - 1 - i)
        position += 1  # because it's 1-based
        positions += [position]

    return ' '.join(str(pos) for pos in positions)



def read_case(lines: List[str]) -> Case:
    """Read a test case from the input."""
    return Case(*(int(num) for num in lines.pop(0).strip().split()))


def read_file(filepath: str) -> List[Case]:
    """Read the input `filepath` and return a list of cases."""
    cases = []
    with open(filepath, 'rt') as fobj:
        lines = fobj.readlines()
        num_cases = int(lines.pop(0))
        for _ in range(num_cases):
            cases.append(read_case(lines))
    return cases


def write_results(results: List, outfile: str) -> None:
    with open(outfile, 'wt') as f:
        for idx, result in enumerate(results):
            f.write('Case #{}: {}\n'.format(idx + 1, result))


@contextmanager
def timing(prefix):
    start = time.time()
    yield
    print('{} took {} seconds.'.format(prefix, time.time() - start))


def main(infile: str, outfile: str) -> None:
    cases = read_file(infile)
    results = []
    for idx, case in enumerate(cases):
        with timing("Solving case #{}".format(idx + 1)):
            results.append(solve(case))
    write_results(results, outfile)


test_cases = {
    Case(k=2, c=3, s=2): '3',
    Case(k=1, c=1, s=1): '1',
    Case(k=2, c=1, s=1): 'IMPOSSIBLE',
    Case(k=2, c=1, s=2): '1 2',
    Case(k=3, c=2, s=3): '2 7',
}


@pytest.mark.parametrize(('case', 'result'), test_cases.items())
def test_function(case: Case, result):
    assert solve(case) == result


if __name__ == '__main__':
    if INPUT_TYPE:
        main(os.path.join('io', '{}.in'.format(INPUT_TYPE)),
             os.path.join('io', '{}.out'.format(INPUT_TYPE)))
    pytest.main(args=[__file__])
