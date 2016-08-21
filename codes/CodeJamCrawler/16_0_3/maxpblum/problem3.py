class Primes(object):
    def __init__(self):
        self.highest_searched = 3
        self.primes = set((2, 3))

    def push_to(self, limit):
        while self.highest_searched + 2 <= limit:
            self.highest_searched += 2
            for p in self.primes_in_order():
                if p > self.highest_searched ** 0.5:
                    self.primes.add(self.highest_searched)
                    break
                if self.highest_searched % p == 0:
                    break

    def primes_in_order(self):
        yield 2
        x = 3
        while True:
            if x in self.primes:
                yield x
            x += 2
            self.push_to(x)

    def first_prime_factor(self, num):
        self.push_to(num ** 0.5)
        if num in self.primes:
            return None
        for p in self.primes_in_order():
            if num % p == 0:
                return p
        return None

primes = Primes().primes_in_order()


def interpret_in_base(num, base):
    digits = (int(d) for d in str(num)[::-1])
    return sum(dig * base ** power for power, dig in enumerate(digits))


def next_binary(b):
    for i, v in enumerate(int(d) for d in str(b)[::-1] + '0'):
        if v == 0:
            return b + (10 ** i) - int('1' * i if i > 0 else 0)


def binaries_of_length(l):
    x = 0
    sx = str(x)
    while len(sx) <= l:
        yield ('0' * (l - len(sx))) + sx
        x = next_binary(x)
        sx = str(x)


def jamcoins_of_length(l):
    if l == 2:
        yield 11
    else:
        binaries = binaries_of_length(l - 2)
        for _ in xrange(2 ** (l - 2)):
            yield int('1' + binaries.next() + '1')


def breadth_first(l, count):
    jamcoins = []
    cands = tuple(jamcoins_of_length(l))
    factors = tuple(
        list(interpret_in_base(c, b)
             for b in xrange(2, 11))
        for c in cands
    )
    for p in primes:
        for i, f_list in enumerate(factors):
            for j, interpreted in enumerate(f_list):
                if interpreted > 0 and \
                        p < interpreted ** 0.5 and \
                        interpreted % p == 0:
                    f_list[j] = -p
            if sum(f_list) < 0:
                jamcoins.append((cands[i], tuple(-f for f in f_list)))
                if len(jamcoins) == count:
                    for c, fs in jamcoins:
                        for i, f in enumerate(fs):
                            assert interpret_in_base(c, i + 2) % f == 0
                    return jamcoins


if __name__ == '__main__':
    repetitions = int(raw_input())
    for r in xrange(1, repetitions + 1):
        str_input = raw_input()
        jc_length, jc_count = tuple(int(n) for n in str_input.split(' '))
        print 'Case #{0}:'.format(r)
        for cand, factors in breadth_first(jc_length, jc_count):
            print '{0} {1}'.format(
                cand,
                ' '.join(str(f) for f in factors)
            )
