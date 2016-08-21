import os
import time
import pytest
import collections
from contextlib import contextmanager
from typing import List


INPUT_TYPE = 'large'


Case = collections.namedtuple('Case', ['s'])

numbers = (
    ('X', collections.Counter('SIX'), 6),
    ('S', collections.Counter('SEVEN'), 7),
    ('G', collections.Counter('EIGHT'), 8),
    ('V', collections.Counter('FIVE'), 5),
    ('F', collections.Counter('FOUR'), 4),
    ('Z', collections.Counter('ZERO'), 0),
    ('W', collections.Counter('TWO'), 2),
    ('I', collections.Counter('NINE'), 9),
    ('O', collections.Counter('ONE'), 1),
    ('T', collections.Counter('THREE'), 3),
)


def solve(case: Case):
    """break 'case', solve and return the solution"""

    digits = []
    letters = collections.Counter(case.s)
    for number in numbers:
        telling_letter, all_letters, digit = number
        while telling_letter in letters and letters[telling_letter] != 0:
            digits.append(digit)
            letters.subtract(all_letters)

    return ''.join(str(d) for d in sorted(digits))


def read_case(lines: List[str]) -> Case:
    """Read a test case from the input."""
    return Case(s=lines.pop(0))


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
    Case(s="OZONETOWER"): "012",
    Case(s="WEIGHFOXTOURIST"): "2468",
    Case(s="OURNEONFOE"): "114",
    Case(s="ETHER"): "3",
}


@pytest.mark.parametrize(('case', 'result'), test_cases.items())
def test_function(case: Case, result):
    assert solve(case) == result


if __name__ == '__main__':
    if INPUT_TYPE:
        main(os.path.join('io', '{}.in'.format(INPUT_TYPE)),
             os.path.join('io', '{}.out'.format(INPUT_TYPE)))
    pytest.main(args=[__file__])
