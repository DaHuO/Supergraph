#!/usr/bin/env python3

import sys
import math

def get_letter_counts(s):
    l_counts = {}
    for l in s:
        if l not in l_counts:
            l_counts[l] = 1
        else:
            l_counts[l] += 1
    return l_counts

def take_digit(l_counts, digit_l_counts, times):
    for l in digit_l_counts.keys():
        l_counts[l] -= digit_l_counts[l]*times

def try_digit(d_counts, l_counts, digit_l_counts, letter, digit):
    if letter in l_counts and l_counts[letter] > 0:
        d_counts[digit] = l_counts[letter]
        take_digit(l_counts, digit_l_counts[digit], l_counts[letter])

def get_the_digits(s):
    spell_digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    l_counts = get_letter_counts(s)
    digit_l_counts = {i : get_letter_counts(d) for i, d in enumerate(spell_digits)}
    d_counts = {d : 0 for d in range(0, 10)}
    
    try_digit(d_counts, l_counts, digit_l_counts, 'Z', 0)
    try_digit(d_counts, l_counts, digit_l_counts, 'W', 2)
    try_digit(d_counts, l_counts, digit_l_counts, 'U', 4)
    try_digit(d_counts, l_counts, digit_l_counts, 'X', 6)
    try_digit(d_counts, l_counts, digit_l_counts, 'G', 8)

    # Now we need 1, 3, 5, 7, 9

    # With Four gone, Three is the only digit left with an R
    try_digit(d_counts, l_counts, digit_l_counts, 'R', 3)

    # With Six gone, Seven is the only digit left with a S
    try_digit(d_counts, l_counts, digit_l_counts, 'S', 7)

    # With Seven gone, Five is the only digit left with a V
    try_digit(d_counts, l_counts, digit_l_counts, 'V', 5)

    # One is the only digit left with an O
    try_digit(d_counts, l_counts, digit_l_counts, 'O', 1)

    # Nine is the only digit left, count the I's
    try_digit(d_counts, l_counts, digit_l_counts, 'I', 9)
    #d_counts[9] = l_counts['I']
    #take_digit(l_counts, digit_l_counts[9])

    digits = []
    for digit, count in d_counts.items():
        for _ in range(count):
            digits.append(digit)
    return sorted(digits)
    

def main():
    if len(sys.argv) < 2:
        print("Usage: get_the_digits.py <file>")
        exit()
    in_file = sys.argv[1]
    with open(in_file) as f:
        cases = int(f.readline())
        for i in range(0, cases):
            s = f.readline().strip() # Strip off the newline
            print("Case #%d: %s" % (i+1, "".join([str(d) for d in get_the_digits(s)])))

##########

if __name__ == '__main__':
    main()
