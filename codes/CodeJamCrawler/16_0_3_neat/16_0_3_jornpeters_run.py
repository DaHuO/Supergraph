import numpy as np
import sys
from sympy.ntheory import factorint
from sympy.ntheory.primetest import isprime


def naive_search(M, N, J):
    p = np.array([0]*N)
    p[0], p[-1] = 1, 1
    jamcoins = []
    proofs = []
    for i in range(0, 2**(N-2)):
        p_ = [int(a) for a in str(bin(i))[2:]]
        p[-(len(p_)+1):-1] = p_
        c = [sum([a*b for a, b in zip(p, D)]) for D in M]
        if all([not isprime(a) for a in c]):
            jamcoins.append("".join([str(a) for a in p]))
            proofs.append([min(list(factorint(a).keys())) for a in c])
            if len(jamcoins) == J:
                break
    return jamcoins, proofs


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        T = int(f.readline())
        N, J = [int(a) for a in f.readline().split()]

    M = []
    for i in range(2, 11):
        M += [[i**a for a in range(N-1, -1, -1)]]

    jamcoins, proofs = naive_search(M, N, J)

    print("Case #1:")
    for j, prfs in zip(jamcoins, proofs):
        print("{} {}".format(j, " ".join([str(a) for a in prfs])))
