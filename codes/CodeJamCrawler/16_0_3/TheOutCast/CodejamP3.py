from math import sqrt; from itertools import count, islice, product
import itertools
from functools import lru_cache, reduce
from collections import Counter
 
 
MUL = int.__mul__
 
 
def prime_factors(n):
    'Map prime factors to their multiplicity for n'
    d = _divs(n)
    d = [] if d == [n] else (d[:-1] if d[-1] == d else d)
    pf = Counter(d)
    return dict(pf)
 
@lru_cache(maxsize=None)
def _divs(n):
    'Memoized recursive function returning prime factors of n as a list'
    for i in range(2, int(sqrt(n)+1)):
        d, m  = divmod(n, i)
        if not m:
            return [i] + _divs(d)
    return [n]
 
 
def proper_divs(n):
    '''Return the set of proper divisors of n.'''
    pf = prime_factors(n)
    pfactors, occurrences = pf.keys(), pf.values()
    multiplicities = product(*(range(oc + 1) for oc in occurrences))
    divs = {reduce(MUL, (pf**m for pf, m in zip(pfactors, multis)), 1)
            for multis in multiplicities}
    try:
        divs.remove(n)
    except KeyError:
        pass
    return divs or ({1} if n != 1 else set())
 
def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def gen(n):
    for i in range(1, 2**n):
        yield '{:0{n}b}'.format(i, n=n)

def bitGen(n):
    return (''.join(i) for i in itertools.product('01', repeat=n))

def divs(n, m):
    if m == 1: return [1]
    if n % m == 0: return [m] + divs(n, m - 1)
    return divs(n, m - 1)
def divisorGenerator(n):
    for x in reversed(divs(n, n)):
        yield x


def coinjam(x):
    nont=[]
    if(x[0]=='1' and x[len(x)-1]=='1'):
        for i in range(2,11):
            if(isPrime(int(x,i))):
                return False
        for i in range(2,11):
            y=list(proper_divs(int(x,i)))
            y.pop(0)
            for suby in y:
                if(suby !=int(x,i) and suby!=1):
                    nont.append(suby)
                    break
        return nont
output="Output-CodeJam-P3.txt"
def callcoin(n,j):
    with open(output, "a") as text_file:
        print("Case #1:",file=text_file)
    y=list(bitGen(n-2))
    counter=0
    for i in y:
        if(counter==j):
            break
        x="1{0}1".format(i)
        L=coinjam(x)
        if(L!=False):
            counter=counter+1
            with open(output, "a") as text_file:
                print(x, end=" ",file=text_file)
                for a in L:
                    print(a, end=" ",file=text_file)
                print("",file=text_file)

callcoin(16,50)
