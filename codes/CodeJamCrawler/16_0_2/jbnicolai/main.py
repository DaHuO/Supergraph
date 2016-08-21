import fileinput
import itertools
import sys

T = int(next(sys.stdin))

for t, S in enumerate(itertools.islice((S.strip() for S in sys.stdin), T), 1):

    alternations = 0 if S[-1] is '+' else 1
    prev = S[0]

    for s in S[1:]:
        if s is not prev:
            alternations += 1
            prev = s

    print('Case #{:d}: {:d}'.format(t, alternations))
