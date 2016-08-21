import sys
from copy import copy
from itertools import product
import numpy as np

test_path = 'D-test.in'
basestring = (str, bytes)


def main(input_path=test_path):
    with open(input_path) as f:
        T = int(f.readline().strip())
        for t in range(T):
            K, C, S = [int(i) for i in f.readline().strip().split(' ')]
            print("Case #{0}: {1}".format(t + 1, ' '.join([str(ans + 1) for ans in solve_n(K, C, S)])))


def solve_n(K, C, S):
    return range(K)

def solve_t(K, C, S):
    return [i * K for i in range(C + 1)]

def solve(K, C, S):
    init_universe = product(range(2), repeat=K)
    all_fractals = []
    for f in init_universe:
        fractal = complexify(f, C)
        all_fractals.append(fractal)

    w = []
    fractals = np.array(all_fractals)
    while fractals.shape[0] > 1:
        candidate_ix = fractals.sum(axis=0).argmax()
        w.append(candidate_ix + 1)
        fractals = fractals[fractals[:, candidate_ix] == 0]

    assert not fractals.any()

    if len(w) > S:
        return 'IMPOSSIBLE'
    else:
        return ' '.join(map(str, w))


def complexify(original, c):
    # L = 0, G = 1
    k = len(original)
    orig_ls = list(original)
    fractal = copy(orig_ls)

    while c > 1:
        for ix, e in enumerate(fractal):
            if e == 0:
                fractal[ix] = orig_ls
            elif e == 1:
                fractal[ix] = [1] * k
            else:
                raise Exception("FUUUUCK")
        fractal = flatten(fractal)
        c -= 1
    return fractal


def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
