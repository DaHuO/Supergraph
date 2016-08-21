#!/usr/bin/env python

"""
Problem

A jamcoin is a string of N >= 2 digits with the following properties:

Every digit is either 0 or 1.
The first digit is 1 and the last digit is 1.
If you interpret the string in any base between 2 and 10, inclusive, the resulting number is not prime.
Not every string of 0s and 1s is a jamcoin. For example, 101 is not a jamcoin;
its interpretation in base 2 is 5, which is prime. But the string 1001 is a jamcoin:
in bases 2 through 10, its interpretation is 9, 28, 65, 126, 217, 344, 513, 730, and 1001,
respectively, and none of those is prime.

We hear that there may be communities that use jamcoins as a form of currency.
When sending someone a jamcoin, it is polite to prove that the jamcoin is legitimate
by including a nontrivial divisor of that jamcoin's interpretation in each base from 2 to 10.
(A nontrivial divisor for a positive integer K is some positive integer other than 1 or K
that evenly divides K.) For convenience, these divisors must be expressed in base 10.

For example, for the jamcoin 1001 mentioned above, a possible set of nontrivial divisors
for the base 2 through 10 interpretations of the jamcoin would be: 3, 7, 5, 6, 31, 8, 27, 5, and 77, respectively.

Can you produce J different jamcoins of length N, along with proof that they are legitimate?

Input

The first line of the input gives the number of test cases, T. T test cases follow;
each consists of one line with two integers N and J.

Output

For each test case, output J+1 lines. The first line must consist of only Case #x:,
where x is the test case number (starting from 1). Each of the last J lines must
consist of a jamcoin of length N followed by nine integers. The i-th of those nine
integers (counting starting from 1) must be a nontrivial divisor of the jamcoin when
the jamcoin is interpreted in base i+1.

All of these jamcoins must be different. You cannot submit the same jamcoin in
two different lines, even if you use a different set of divisors each time.

Limits

T = 1. (There will be only one test case.)
It is guaranteed that at least J distinct jamcoins of length N exist.

Small dataset

N = 16.
J = 50.
Large dataset

N = 32.
J = 500.
Note that, unusually for a Code Jam problem, you already know the exact contents of each input file.
For example, the Small dataset's input file will always be exactly these two lines:

1
16 50
So, you can consider doing some computation before actually downloading an input file and starting the clock.
"""

import itertools
import math

# If we haven't found one by here, just move along and save time.
STOP_AT_DIVISOR = 1000

def get_jamcoins_to_try_small(length):
    # The first and last digits must be 1, which leaves us with 2**(length-2) options
    for jamcoin_index in xrange(long(math.pow(2, length - 2))):
        # We convert this index to binary, but it will be like "0bXYXYXYXYXYX"
        # so we strip the "0b".
        mid_string = bin(jamcoin_index)[2:]
        # But this won't have all the digits we desire necessarily, so we pad on
        # the left.
        padded_mid_string = "{{:0>{}}}".format(length - 2).format(mid_string)
        full_string = "1" + padded_mid_string + "1"
        # print "xcxc trying:", full_string
        yield full_string

def get_jamcoins_to_try_very_manual(length):
    # The first and last digits must be 1

    # We want the sum of the digits to be a multiple of 2 and 3, ie 6, which will
    # give us divisibility in bases 3, 4, 5, 7, 9, and 10, and fairly quickly.
    # So we're just left to non-trivially check bases 2, 6, 8.

    # We do a funky iteration to ensure we have digits "1111", possibly with some
    # space inbetween, and padded on the left with 0's.
    for zeroes_gap1 in range(0, length - 5):
        for zeroes_gap2 in range(0, length - 5 - zeroes_gap1):
            for zeroes_gap3 in range(0, length - 5 - zeroes_gap1 - zeroes_gap2):
                space_left_right = length - 6 - zeroes_gap1 - zeroes_gap2 - zeroes_gap3
                for zeroes_left in range(0, space_left_right + 1):
                    zeroes_right = space_left_right - zeroes_left
                    jamcoin_middle = "{left}1{gap1}1{gap2}1{gap3}1{right}".format(
                        left="0" * zeroes_left,
                        gap1="0" * zeroes_gap1,
                        gap2="0" * zeroes_gap2,
                        gap3="0" * zeroes_gap3,
                        right="0" * zeroes_right,
                    )
                    full_string = "1" + jamcoin_middle + "1"
                    print "xcxc trying:", full_string
                    yield full_string

def get_jamcoins_to_try(length):
    # Take the jamcoins to try we got from our original method, but skip those
    # that don't have digits summing to a multiple of 6. This will be a little less
    # manual, and maybe give us a greater set?
    for jamcoin in get_jamcoins_to_try_small(length):
        if sum(int(c) for c in jamcoin) % 6 == 0:
            yield jamcoin

def get_and_print_jamcoins(length, num_examples):
    """
    length: INT jamcoins should be this long, ie 6 -> "100011" for example
    num_examples: INT how many to get and print
    """
    jamcoins_found = 0
    for potential_jamcoin in get_jamcoins_to_try(length):
        divisors_or_false = get_divisors_if_valid(potential_jamcoin)
        if divisors_or_false:
            full_line = [potential_jamcoin] + divisors_or_false
            full_line_as_str = " ".join(str(item) for item in full_line)
            print full_line_as_str
            jamcoins_found += 1
            if jamcoins_found == num_examples:
                return

def get_divisors_if_valid(potential_jamcoin):
    divisors = []
    for base in range(2, 11):
        new_divisor = get_divisor_for_base(potential_jamcoin, base)
        if new_divisor is None:
            return False
        divisors.append(new_divisor)

    return divisors

def get_divisor_for_base(potential_jamcoin, base):
    value_in_base = long(potential_jamcoin, base)
    for potential_divisor in itertools.chain(
        [2],
        xrange(3, long(math.sqrt(value_in_base)) + 1, 2)
    ):
        if value_in_base % potential_divisor == 0:
            return potential_divisor
        if potential_divisor > STOP_AT_DIVISOR:
            break

    return None


if __name__ == "__main__":
    t = int(raw_input())
    n, j = [int(x) for x in raw_input().split(" ")]
    print "Case #1:"
    get_and_print_jamcoins(n, j)
