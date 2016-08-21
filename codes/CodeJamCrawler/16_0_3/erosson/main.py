# https://code.google.com/codejam/contest/6254486/dashboard#s=p2
import sys
import pyprimes

factor_primes = list(pyprimes.primes_below(pyprimes.nth_prime(1e5)))

def log(*messages):
    return # silent
    for message in messages:
        print message,
    print

class CoinCandidate(object):
    def __init__(self, value):
        self.value = value
        self.bases = range(2, 10+1)
        self.base_values = dict((i, int(self.value, i)) for i in self.bases)
        self.base_divisors = dict()
        self.prime_bases = set()

    def is_invalid(self):
        return len(self.prime_bases) > 0

    def is_valid(self):
        # 2 - 10
        return len(self.base_divisors) == 9

    def is_done(self):
        return self.is_valid() or self.is_invalid()

    def list_divisors(self):
        return [self.base_divisors[i] for i in self.bases]

    def _factor_base(self, base):
        val = self.base_values[base]
        # self.base_divisors[base] = next(pyprimes.factorise(val))[0]
        # self.base_divisors[base] = pyprimes.factors(self.base_values[base])

        # We know a factor exists from isprime, but we don't know what it is.
        # isprime uses magic probabilistic prime-finding (with no false positives but some false negatives).
        # factoring can be slow. factor manually, and give up if factors are too large
        for factor in factor_primes:
            # print val, factor, val%factor==0
            if val % factor == 0:
                self.base_divisors[base] = factor
                return
        # no reasonable-sized factors found
        self.prime_bases.add(base)

    def evaluate(self):
        for base, value in self.base_values.items():
            # this may skip some valid coins, that's fine
            # TODO: is it fast enough?
            if pyprimes.isprime(value):
                self.prime_bases.add(base)
                assert self.is_invalid()
                break
        if not self.is_invalid():
            log('factoring...', self.value)
            # find one factor for valid coins
            for base in self.bases:
                if self.is_invalid():
                    break
                # log('factoring...', self.value, base)
                self._factor_base(base)
        assert self.is_done()

    def __str__(self):
        # log(self.value, self.list_divisors())
        return '%s %s' % (self.value, ' '.join(str(n) for n in self.list_divisors()))
    
def candidates(length):
    for i in xrange(pow(2,length-2)):
        # https://stackoverflow.com/questions/16926130/python-convert-to-binary-and-keep-leading-zeros
        yield CoinCandidate('1%s1' % format(i, '0%db'%length)[2:])

def run(coinlength, numcoins):
    ret = []
    # numcoins=100
    for candidate in candidates(coinlength):
        candidate.evaluate()
        if candidate.is_done() and candidate.is_valid():
            assert not candidate.is_invalid()
            ret.append(str(candidate))
            log('valid', candidate.value, '%d/%d' % (len(ret), numcoins))
        else:
            log('invalid', candidate.value, '%d/%d' % (len(ret), numcoins))
            pass
        if len(ret) >= numcoins:
            break
    return '\n'.join(ret)

def parse(lines):
    (n, j) = (int(x) for x in lines.pop(0).split())
    return dict(coinlength=n, numcoins=j)

def main(infile):
    lines = infile.readlines()
    count = int(lines.pop(0))
    cases = (parse(lines) for case in range(count))
    output = (run(**case) for case in cases)
    for i, result in enumerate(output):
        print "Case #%d: \n%s" % (i + 1, result)

if __name__=='__main__':
    main(sys.stdin)
