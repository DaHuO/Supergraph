#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def convert_boolarray_digit(boolarray):
    digit = 0
    for k, b in enumerate(boolarray):
        digit += b*10**(boolarray.size-k-1)
    return digit


def get_non_prime_solver(digit_size, how_many):

    found_digits = []
    dividers = []
    # becaue digit_size is quite bit, I rely on random generation
    n_got = 0
    while n_got < how_many:

        r = np.random.rand(digit_size - 2)
        r = r > 0.5
        boolarray = np.append(np.append(True, r), True)
        try_digit = convert_boolarray_digit(boolarray)

        if try_digit not in found_digits:  # due to avoid duplicate
            is_all_non_prime, non_trivial_dividers = check_all_bases(try_digit)
            if is_all_non_prime:
                n_got += 1
                found_digits.append(try_digit)
                dividers.append(non_trivial_dividers)
                print "%d" % try_digit,
                print ' '.join(map(str, non_trivial_dividers))

    return found_digits, dividers


# return [bool_all_are_non_prime, non_trivial_dividers] = check_all_bases(digit)
def check_all_bases(digit):
    # for b in xrange(2,10):
    numbers = [convert_with_base(digit, base) for base in xrange(2, 11)]
    chk = [is_prime(number) for number in numbers]
    is_there_prime = [c[0] for c in chk]
    dividers = [c[1] for c in chk]
    return sum(is_there_prime)==0, dividers


def convert_with_base(digit, base):
    digit_str = str(digit)
    num = 0
    for k in xrange(len(digit_str)):
        d = int(digit_str[k])
        num += d*base**(len(digit_str)-k-1)
    return num


def is_prime(number):
    b_is_prime = True
    divider = None
    for i in xrange(2, min(number,60000)): # cannot go further
        mod = number % i
        if mod==0:
            b_is_prime = False
            divider = i
            break

    #
    # is_prime = all(mods)
    # # divider = [i for i, m in enumerate(mods) if m == 0]
    # # divider = divider + 2
    # divider = None
    #
    # if ~is_prime:
    #     for i, m in enumerate(mods):
    #         if m == 0:
    #             divider = i+2
    #             break

    return b_is_prime, divider


if __name__ == "__main__":

    testcases = input()
    for caseNr in xrange(1, testcases+1):
        line = raw_input().split()
        digit_size = int(line[0])
        how_many = int(line[1])
        print "Case #%i:" % caseNr
        digits, dividers = get_non_prime_solver(digit_size, how_many)