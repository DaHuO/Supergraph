from itertools import product
from itertools import *
from collections import defaultdict

def main(filename):
    f = iter(open(filename, "r").readlines())

    t = int(next(f))
    for e, _ in enumerate(range(t)):
        word = next(f).strip()
        print("Case #{}: {}".format(e+1, find(None, word)))

import sys
sys.setrecursionlimit(1500)


def find(cur, rest):
    if cur is None:
        if len(rest) < 2:
            return rest

        return find(sorted(list(rest[:2]), reverse=True), rest[2:])

    if not rest:
        return "".join(cur)

    head = rest[0]

    if head >= cur[0]:
        return find([head] + cur, rest[1:])
    else:
        return find(cur + [head], rest[1:])







if __name__ == "__main__":

    filename = "test"
    filename = "A-small-attempt0.in"
    filename = "A-large.in"

    

    main(filename)





