#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

"""
Solution for Google Code Jam 2016 - Qualification Round - A: Counting Sheep
Usage: sheep_counter.py $in_file $out_file
    in_file = file containing input per the description
    out_file = writable file to write the results to

Problem Summary:
    Given a number n, iterate through it's multiples until each digit 0-9 has been in on of the multiples
    the answer is the multiple that completes the set of encountered digits
    for numbers where all digits will never be encountered return INSOMNIA

Output format:
    CASE N#: $ANSWER

Input format:
    T - number of cases
    T Lines of N
"""

import sys

def solve(n):
    """Determine the multiple that completes the set of digits.
        n - the number to solve for
    """
    # limited to running through 1000 multiples
    encountered = set()
    i = 1
    while True:
        digits = set(str(n * i))
        for d in digits:
            encountered.add(d)
        if len(encountered) == 10:
            return n * i
        i += 1
        if i == 1001:
            break
    return "INSOMNIA"

def format_answer(t, a):
    """Return a string that's formatted to be printed to the file
        t- the case number; 1 is added since the loop starts at 0
        a- the answer for the case
    """
    return "Case #{}: {}\n".format(t + 1, a)


try:
    in_file = open(sys.argv[1], 'r')
    out_file = open(sys.argv[2], 'w')
except:
    print("Usage:\n\tsheep_counter.py $in_file $out_file")
    print("INFILE: {}\n{}\nOUTFILE: {}\n{}\n".format(sys.argv[1], sys.argv[2], in_file, out_file))
    exit()

case_count = int(in_file.readline())
for t in range(case_count):
    case = int(in_file.readline())
    answer = solve(case)
    formatted = format_answer(t, answer)
    out_file.write(formatted)
in_file.close()
out_file.close()
