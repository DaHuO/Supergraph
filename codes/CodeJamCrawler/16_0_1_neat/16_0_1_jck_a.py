import fileinput
import os
from pathlib import Path

from itertools import count

def main(n):
    if n == 0:
        return 'INSOMNIA'
    seen = set()
    for n in count(n, n):
        seen |= set(str(n))
        if len(seen) == 10:
            return n

if __name__ == '__main__':
    f = fileinput.input()
    t = int(next(f))
    op = open(Path(fileinput.filename()).with_suffix('.out').name, mode='w')
    for i, l in enumerate(f, 1):
        print('Case #{}: {}'.format(i, main(int(l))), file=op)
