#!/usr/bin/env python

"""
Problem

Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster.
First, she picks a number N. Then she starts naming N, 2 x N, 3 x N, and so on.
Whenever she names a number, she thinks about all of the digits in that number.
She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen
at least once so far as part of any number she has named. Once she has seen each
of the ten digits at least once, she will fall asleep.

Bleatrix must start with N and must always name (i + 1) x N directly after i x N.
For example, suppose that Bleatrix picks N = 1692. She would count as follows:

N = 1692. Now she has seen the digits 1, 2, 6, and 9.
2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
3N = 5076. Now she has seen all ten digits, and falls asleep.
What is the last number that she will name before falling asleep? If she will count forever, print INSOMNIA instead.

Input

The first line of the input gives the number of test cases, T.
T test cases follow. Each consists of one line with a single integer N, the number Bleatrix has chosen.

Output

For each test case, output one line containing Case #x: y, where x is the test
case number (starting from 1) and y is the last number that Bleatrix will name
before falling asleep, according to the rules described in the statement.

Limits

1 <= T <= 100.
Small dataset

0 <= N <= 200.
Large dataset

0 <= N <= 10e6.
"""

MAX_NUM_ITERATIONS = 100
DIGITS_STR = "1234567890"

def get_last_num(first_num):
    record = {c: False for c in DIGITS_STR}
    for num_iteration in range(1, MAX_NUM_ITERATIONS + 1):
        current_num = first_num * num_iteration
        record = get_updated_record(current_num, record)
        if is_complete(record):
            return current_num

    # print "xcxc still missing %s after %s tries" % (
    #     [k for k, v in record.iteritems() if not v], num_iteration
    # )
    return "INSOMNIA"


def get_updated_record(current_num, record):
    """
    current_num: latest num counted
    record: dict to update
    """
    update = {c: True for c in str(current_num) if c in DIGITS_STR}
    record.update(update)
    return record


def is_complete(record):
    return all(record.values())


if __name__ == "__main__":
    t = int(raw_input())
    for case_num in range(1, t + 1):
        n = long(raw_input())
        print "Case #{}: {}".format(case_num, get_last_num(n))