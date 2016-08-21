from math import sqrt
import pickle
from itertools import chain


def resolve(line):
    N, J = map(int, line.split())
    c = 1
    for jc in gen_jamcoins(N):
        t = test(jc)
        if t:
            print jc, t
            if c == J:
                break
            c += 1


def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for i, isprime in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False


primes = pickle.load(open('primes.pkl'))

# primes.pkl was generated like this:
# primes = list(primes_sieve(333333333))
# pickle.dump(primes, open('primes.pkl', 'w'))

def test(jc):
    ds = []
    for b in range(2, 11):
        n = tobase(jc, b)
        # for i in chain(primes, xrange(primes[-1], int(sqrt(n))+2)):
        for i in primes:
            if not n % i:
                ds.append(i)
                break
        else:
            return None

    return ' '.join(map(str, ds))
     

def gen_jamcoins(N):
    assert N >= 2
    if N == 2:
        return ['11']
    return ('1{}1'.format(tobin(i, N-2)) for i in xrange(2**(N-2)))


def tobin(n, just):
    return bin(n)[2:].rjust(just, '0')


def tobase(jc, b):
    m = len(jc)
    return sum(b**(m-i-1) for i, el in enumerate(jc) if el == '1')


# Handle IO


def main():
    get_line()  # dicard first
    print 'Case #1:'
    resolve(get_line())


def get_line():
    try:
        return raw_input()
    except EOFError:
        return None


if __name__ == '__main__':
    main()
