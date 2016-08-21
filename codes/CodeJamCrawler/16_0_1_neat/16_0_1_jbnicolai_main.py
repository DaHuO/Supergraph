import fileinput
import itertools
import sys

T = int(next(sys.stdin))

for t, N in enumerate(itertools.islice((int(line) for line in sys.stdin), T), 1):
    if N is 0:
        print('Case #{:d}: INSOMNIA'.format(t))
    else:
        digits = set()
        i = 0
        while len(digits) < 10:
            i += 1
            digits.update(set(str(i * N)))
        print('Case #{:d}: {:d}'.format(t, i * N))
