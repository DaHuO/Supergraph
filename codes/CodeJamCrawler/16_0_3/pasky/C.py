import sympy
import primefac
import itertools

def to_base(b, v):
    p = 1
    res = 0
    while v > 0:
        if v % 2 != 0:
            res += p
        p *= b
        v /= 2
    return res
            
    
def gen_jams(N):
    for p in itertools.count(2**(N-1) + 1, 2):
        ok = True
        for base in xrange(2, 11):
            v = to_base(base, p)
            if primefac.isprime(v):
                ok = False
                break
        if ok:
            yield p

def get_divisors(p):
    for base in xrange(2, 11):
        v = to_base(base, p)
        yield primefac.mpqs(v)        
    
def go(f, N, J):
    f.write('Case #1:\n')
    jams = gen_jams(N)
    bad = [0b1000000000111101, 0b1000000001111001, 0b1000000010010111, 0b10000000000000000000000010110101, 0b10000000000000000000000011000001, 0b10000000000000000000010010010011]
    jams = itertools.ifilter(lambda x: x not in bad, jams)
    for p in itertools.islice(jams, 0, J):        
        print bin(p),
        f.write('{} {}\n'.format(bin(p)[2:], ' '.join(map(str, get_divisors(p)))))
        print
        f.flush()

def main():
    with open('C-small-attempt1.out', 'wb') as f:
        go(f, 16, 50)
    with open('C-large.out', 'wb') as f:
        go(f, 32, 500)    
    

if __name__ == '__main__':
    main()
