from sys import stdin
from itertools import count

test_cases = int(raw_input())

for i, N in enumerate(stdin):
    print "Case #%d:"%(i + 1),

    digits = set()
    repeating = 0
    for j in count(1):
        case = str(int(N) * j)

        digits_before = len(digits)
        digits.update(case)

        repeating += int(digits_before == len(digits))
        if len(digits) >= 10:
            print case
            break

        if repeating >= 1000:
            print "INSOMNIA"
            break

