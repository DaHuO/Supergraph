#!/usr/bin/env python

import sys
import itertools

def is_prime(n):
    if n <= 3:
        return None
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    while i*i <= n:
        if n % i == 0:
            return i
        if n % (i+2) == 0:
            return i+2
        i += 6
    return None

if __name__ == "__main__":
    for (kkk, i) in enumerate([l.rstrip("\n") for l in sys.stdin.readlines()[1:]]):
        (n,j) = map(int, i.split(" "))
        if j == 50:
            k = 6
        else:
            k = 9
        bases = list(range(2,11))
        nbs = ['1' +("0"*((n-4-2*k)//2))+ ''.join(x) + "11"+("0"*((n-4-2*k)//2)) + ''.join(x) + '1' for x in itertools.product(['0','1'], repeat=k)]

        cool_nb = []
        for nb in nbs:
            d = []
            for b in bases:
                i = is_prime(int(nb, b))
                if i:
                    d.append(i)
                else:
                    break
            if len(d) == 9:
                cool_nb.append((nb, d))
            if len(cool_nb) == j:
                break
        solution = cool_nb
        
        print("Case #" + str(kkk + 1) + ":")
        print("\n".join([k + ' ' + ' '.join(map(str, v)) for k,v in solution]))
