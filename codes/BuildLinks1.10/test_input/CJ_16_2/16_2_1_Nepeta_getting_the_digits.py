"""
Getting the digits
https://code.google.com/codejam/contest/11254486/dashboard
"""

import fileinput
import collections

lines = fileinput.input()

cases = int(next(lines))

for case in range(1, cases + 1):
    s = next(lines).strip()
    counts = collections.Counter(s)
    digits = collections.Counter()

    # Remove zero's
    counts['E'] -= counts['Z']
    counts['R'] -= counts['Z']
    counts['O'] -= counts['Z']
    digits[0] = counts['Z']
    counts['Z'] = 0
    # Remove two's
    counts['T'] -= counts['W']
    counts['O'] -= counts['W']
    digits[2] = counts['W']
    counts['W'] = 0
    # Remove four's
    counts['F'] -= counts['U']
    counts['O'] -= counts['U']
    counts['R'] -= counts['U']
    digits[4] = counts['U']
    counts['U'] = 0
    # Remove six's
    counts['S'] -= counts['X']
    counts['I'] -= counts['X']
    digits[6] = counts['X']
    counts['X'] = 0
    # Remove eight's
    counts['E'] -= counts['G']
    counts['I'] -= counts['G']
    counts['H'] -= counts['G']
    counts['T'] -= counts['G']
    digits[8] = counts['G']
    counts['G'] = 0

    # Second layer

    # Remove one's
    counts['N'] -= counts['O']
    counts['E'] -= counts['O']
    digits[1] = counts['O']
    counts['O'] = 0
    # Remove three's
    counts['T'] -= counts['H']
    counts['R'] -= counts['H']
    counts['E'] -= counts['H'] * 2
    digits[3] = counts['H']
    counts['H'] = 0
    # Remove five's
    counts['I'] -= counts['F']
    counts['V'] -= counts['F']
    counts['E'] -= counts['F']
    digits[5] = counts['F']
    counts['F'] = 0
    # Remove seven's
    counts['S'] -= counts['V']
    counts['E'] -= counts['V'] * 2
    counts['N'] -= counts['V']
    digits[7] = counts['V']
    counts['V'] = 0
    # Remove nine's
    counts['N'] -= counts['I'] * 2
    counts['E'] -= counts['I']
    digits[9] = counts['I']
    counts['I'] = 0

    ans = ''.join(str(n) * digits[n] for n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    print("Case #{case}: {ans}".format(**locals()))

