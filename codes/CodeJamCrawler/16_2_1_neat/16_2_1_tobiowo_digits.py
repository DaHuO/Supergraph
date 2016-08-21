"""
Problem

You just made a new friend at an international puzzle conference, and you asked for a way to keep in touch. You found the following note slipped under your hotel room door the next day:

"Salutations, new friend! I have replaced every digit of my phone number with its spelled-out uppercase English representation ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" for the digits 0 through 9, in that order), and then reordered all of those letters in some way to produce a string S. It's up to you to use S to figure out how many digits are in my phone number and what those digits are, but I will tell you that my phone number consists of those digits in nondecreasing order. Give me a call... if you can!"

You would to like to call your friend to tell him that this is an obnoxious way to give someone a phone number, but you need the phone number to do that! What is it?

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S of uppercase English letters.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is a string of digits: the phone number.
"""
import sys
import fileinput
from collections import Counter
import numpy as np

all_digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
digit_sets = [Counter(c) for c in all_digits]
char_list = list(set(''.join(all_digits)))

def get_number(s):
    counter = Counter(s)
    y = np.array([
        counter.get(char, 0)
        for char in char_list
    ])
    x = np.array([
        [digit_set.get(char, 0) for char in char_list]
        for digit_set in digit_sets
    ])
    scalars = np.linalg.lstsq(x.T, y)[0]
    result = []
    for digit, count in enumerate(np.rint(scalars)):
        count = int(count)
        result.append(str(digit) * count)
    return ''.join(result)

for i, line in enumerate(fileinput.input()):
    if fileinput.isfirstline():
        num_cases = int(line)
    else:
        print 'Case #{0}: {1}'.format(i, get_number(line.strip()))