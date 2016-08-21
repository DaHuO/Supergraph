import fileinput
import sys


def flip(P, j):
    def _flip(L):
        new_L = []
        for x in L:
            if x == '+':
                new_L.append('-')
            else:
                new_L.append('+')
        return ''.join(new_L)
    return _flip(P[:j][::-1]) + P[j:]


def get_idx_to_flip(P):
    if all([x == '+' for x in P]):
        return None
    first_char = P[0]
    for j, p in enumerate(P):
        if p != first_char:
            return j
    return len(P)

"""
- | +

-+ | ++

+- | -- | ++

--+- | +++-  | ---- | ++++

-+-+-+ | ++-+-+ | -+-+-- | ++-+-- | +--+-- |  ---+-- | ++++--

"""


def pancakes(P):
    num_flips = 0

    idx = get_idx_to_flip(P)
    while idx is not None:
        P = flip(P, idx)
        num_flips += 1
        idx = get_idx_to_flip(P)

    return num_flips


if __name__ == '__main__':
    i = 0
    for line in fileinput.input():
        if i > 0:
            y = line.strip()
            print 'Case #{}: {}'.format(i, pancakes(y))
        i += 1
