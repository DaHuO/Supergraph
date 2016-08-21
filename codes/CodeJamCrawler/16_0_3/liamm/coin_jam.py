# https://github.com/liam-m/primes.py
from primes import is_prime, pollards_rho

STARTS_WITH_0 = 0
ENDS_WITH_0 = 1
IS_PRIME = 2
ALL_GOOD = 3

# Returns is_jamcoin, reason, evidence
def jamcoin(st):
    if not all(c in ('0', '1') for c in st):
        raise ValueError(st)
    
    if len(st) < 2:
        raise ValueError(st)
    
    if st[0] != '1' or st[-1] != '1':
        return False, STARTS_WITH_0, '0'

    if st[-1] != '1':
        return False, ENDS_WITH_0, '0'

    evidence = []

    for base in range(2, 10+1):
        n = int(st, base)
        if is_prime(n):
            return False, IS_PRIME, base
        else:
            factor = pollards_rho(n)
            evidence.append((base, factor))

    return True, ALL_GOOD, evidence

def candidates(length):
    n = '1' + '0'*(length-2) + '1'

    while True:
        yield n

        n = bin(int(n, 2) + 2)[2:]

        if len(n) > length:
            raise StopIteration

print(jamcoin('100011'))
print(jamcoin('111111'))
print(jamcoin('111001'))
print(jamcoin('110111'))

with open('C-small-attempt0.in.txt') as f, open('C-small-attempt0.out.txt', 'w') as g:
    t = int(f.readline())
    for case_num in range(1, t+1):
        l = f.readline()
        n, j = map(int, l.split(' '))

        g.write("Case #{}:\n".format(case_num))

        for cand in candidates(n):
            is_jamcoin, reason, evidence = jamcoin(cand)

            if is_jamcoin:
                j -= 1
                g.write("{} ".format(cand))
                for base, factor in evidence:
                    g.write("{} ".format(factor))

                g.write("\n")

                if j == 0:
                    break
