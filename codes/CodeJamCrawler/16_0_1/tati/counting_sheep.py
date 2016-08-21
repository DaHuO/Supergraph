#!/usr/bin/env python3
"""
Problem A. Counting Sheep
CodeJam 2016: Qualification Round
https://code.google.com/codejam/contest/6254486/dashboard

Example of how to run:
$ ./counting_sheep.py < sample_input.txt > sample_output.txt

Validate:
$ diff -s sample_output.txt sample_output_key.txt
Files sample_output.txt and sample_output_key.txt are identical
"""
__author__ = "Tatiana Al-Chueyr"
__email__ = "tatiana.alchueyr@gmail.com"
__date__ = "2016-04-09"
__version__ = "1.0.0"


def solve(number):
    """
    Compute the last number that Bleatrix Trotter the sheep sees before
    falling asleep.
    """
    if number == 0:
        return "INSOMNIA"
    else:
        total_digits = 10  # there are 10 digits [0-9]
        digits_seen = set()
        multiplier = 0
        while len(digits_seen) < total_digits:
            multiplier += 1
            digits_in_n = {int(i) for i in str(multiplier*number)}
            digits_seen = digits_seen.union(digits_in_n)
    return multiplier*number


if __name__ == "__main__":
    TOTAL = int(input())
    for i in range(1, TOTAL + 1):
        n = int(input())
        print("Case #{}: {}".format(i, solve(n)))
