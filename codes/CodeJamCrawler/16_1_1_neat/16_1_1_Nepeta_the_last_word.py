"""
The Last Word:
https://code.google.com/codejam/contest/4304486/dashboard
"""

import fileinput

lines = fileinput.input()

cases = int(next(lines))

for case in range(1, cases + 1):
    letters = next(lines).strip()

    word = letters[0]

    high = word
    low = word

    for letter in letters[1:]:
        if letter >= high:
            word = letter + word
        else:
            word = word + letter

        high = max(letter, high)
        low = min(letter, low)

    ans = word

    print("Case #{case}: {ans}".format(**locals()))
