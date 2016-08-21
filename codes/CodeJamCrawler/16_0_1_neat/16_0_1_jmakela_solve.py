# -*- coding: utf-8 -*-

from __future__ import print_function

"""
Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep
faster. First, she picks a number N. Then she starts naming N, 2 × N, 3 × N,
and so on. Whenever she names a number, she thinks about all of the digits in
that number. She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9)
she has seen at least once so far as part of any number she has named. Once she
has seen each of the ten digits at least once, she will fall asleep.

Bleatrix must start with N and must always name (i + 1) × N directly after
i x N. For example, suppose that Bleatrix picks N = 1692. She would count
as follows:

    N = 1692. Now she has seen the digits 1, 2, 6, and 9.
    2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
    3N = 5076. Now she has seen all ten digits, and falls asleep.

What is the last number that she will name before falling asleep? If she will
count forever, print INSOMNIA instead.

Input

The first line of the input gives the number of test cases, T. T test cases
follow. Each consists of one line with a single integer N, the number
Bleatrix has chosen.

Output

For each test case, output one line containing Case #x: y, where x is the
test case number (starting from 1) and y is the last number that Bleatrix will
name before falling asleep, according to the rules described in the statement.

Limits

1 <= T <= 100.

################################################################################
Cases where it does not terminate -
* divisible by 0

"""


def read_all_cases(filename, case_reader):
    with open(filename) as f:
        count = int(f.readline())
        cases = []
        for _ in xrange(count):
            cases.append(case_reader(f))
        return cases


def output_results(results, f):
    for x, r in enumerate(results):
        print("Case #{}: {}".format(x+1, r), file=f)


def test_run(case_reader, run_case, infile, outfile):
    import StringIO

    cases = read_all_cases(infile, case_reader)
    results = map(run_case, cases)
    buf = StringIO.StringIO()
    output_results(results, buf)
    got = buf.getvalue().splitlines()

    with open(outfile) as f:
        expected = [ln.strip() for ln in f.readlines()]

    wrong = 0
    for g, e in zip(got, expected):
        if g != e:
            print("Got '{}', expected '{}'".format(g.strip(), e.strip()))
            wrong += 1
    if not wrong:
        print("Sample: all correct.")


def live_run(case_reader, run_case, infile, outfile):
    cases = read_all_cases(infile, case_reader)
    results = map(run_case, cases)
    with open(outfile, 'w') as f:
        output_results(results, f)
    print("Live run: Done.")


################################################################################
################################################################################
################################################################################


def read_case(f):
    return f.readline().strip()


def run(number):
    seen = {}
    number = int(number)
    if number == 0:
        return 'INSOMNIA'

    def add_chars(num):
        for n in str(num):
            seen[n] = True

    multiplier = 0
    while len(seen) < 10:
        multiplier += 1
        add_chars(number*multiplier)
    return number*multiplier


def main():
    import sys
    if len(sys.argv) >= 2:
        fname = sys.argv[1]
        infile = fname + '.in'
        outfile = fname + '.out'
        live_run(read_case, run, infile, outfile)
    else:
        test_run(read_case, run, 'sample.in', 'sample.out')


if __name__ == '__main__':
    main()
