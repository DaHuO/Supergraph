import sys
import numpy as np
from sympy.ntheory import isprime
from sympy import primefactors

lines = [x.strip() for x in list(sys.stdin.readlines())]

cases = int(lines[0])
lines = lines[1:]

for case_i in range(cases):
    bitLength, samples = [int(x) for x in lines[case_i].split()]

    binaries = []
    for i in range(np.power(2, bitLength-1)+1, np.power(2, bitLength), 2):
        binaries.append(np.binary_repr(i))

    binaries = np.array(binaries)
    base_res = []

    for base in range(2, 11):
        base_res.append([np.int(x, base=base) for x in binaries])

    base_res = np.array(base_res)
    bases, bins = base_res.shape

    vfunc = np.vectorize(lambda x: isprime(x))
    primes = ~vfunc(base_res)
    cols = np.all(primes, axis=0)
    indices = np.argwhere(cols==True).ravel()[:samples]
    mains = base_res[:, indices]
    prifunc = np.vectorize(lambda x: primefactors(x)[-1])
    res = prifunc(mains)
    inds = binaries[indices]

    print ('Case #{}:'.format(case_i+1))
    for ind, r in zip(inds, res.T):
        print ('{} {}'.format(int(ind), " ".join(r.astype(str))))
