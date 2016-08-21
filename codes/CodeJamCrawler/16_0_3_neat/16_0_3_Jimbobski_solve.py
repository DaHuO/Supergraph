
import sys

import numpy as np


def find_divisor(n):
    # Try a simpler version
    divs = np.arange(2, 100)
    #print(n)
    #divs = np.arange(2, n)
    idx = np.where((n % divs) == 0)[0]
    if len(idx) > 0:
        return divs[idx[0]]
    else:
        return None

if __name__ == '__main__':
    f = open(sys.argv[1], 'rt')
    lines = f.readlines()
    f.close()

    cases = [l.strip().split(' ') for l in lines[1:]]
    primes = {}

    for case_i, case in enumerate(cases):
        n_digits, n_coins = int(case[0]), int(case[1])
        #print(n_digits, n_coins)

        num_candidates = 2**(n_digits - 2)

        #print(candidates)
        n_found = 0
        found = []
        #for c in candidates:
        for c in range(num_candidates):
            c = '1' + np.binary_repr(c, n_digits - 2) + '1'
            bases = [int(c, base) for base in range(2, 11)]
            divisors = [0]*9
            for b_i, b in enumerate(bases):
                d = find_divisor(b)
                if d is None:
                    break
                else:
                    #print("Base%i, Number:%i, Divisor: %i" % (b_i+2, b, d))
                    divisors[b_i] = d

            if d is None:
                continue

            #print("Found coin")
            n_found += 1
            found.append((c, divisors))

            if n_found == n_coins:
                break
        #print(found)
        if n_found == n_coins:
            out_str = '\n'.join([' '.join([f[0]] + [str(x) for x in f[1]]) for f in found])
            print("Case #%i:\n %s" % (case_i+1, out_str))
        else:
            print("Case #%i: FAILED" % (case_i+1))
