from math import sqrt
import itertools as it
from random import randint
from functools import wraps
import errno
import os
import signal


class TimeoutError(Exception):
    pass


def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    # from http://stackoverflow.com/a/2282656/1941513
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator


def catch_timeout(seconds, return_on_timeout=(None,) * 9):
    def decorator(f):
        _f = timeout(seconds)(f)

        def wrapper(*args, **kwargs):
            try:
                return _f(*args, **kwargs)
            except TimeoutError:
                return return_on_timeout

        return wraps(f)(wrapper)

    return decorator


def memo(f):
    """memoization decorator, taken from Peter Norvig's Design of Computer
    Programs course on Udacity.com"""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            result = cache[args] = f(*args)
            return result
        except TypeError:  # unhashable argument
            return f(*args)
    return _f


def find_jamcoins(length, number):
    jamcoins = (c for c in candidates(length) if is_jamcoin(c))
    return it.islice(jamcoins, number)


def candidates(length):
    if length is 2:
        yield '11'
    else:
        indexes = range(length - 2)
        for ones in powerset(indexes):
            middle = ''.join('1' if i in ones else '0' for i in indexes)
            yield '1' + middle + '1'


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    # from https://docs.python.org/2/library/itertools.html
    s = list(iterable)
    return it.chain.from_iterable(it.combinations(s, r) for r in xrange(len(s)+1))


def is_jamcoin(candidate):
    return all(divisors(candidate))


@memo
@catch_timeout(1)
def divisors(coin):
    interpretations = (to_base(coin, base) for base in xrange(2, 11))
    is_prime = fermat_primality_test
    # is_prime = fermat_alt
    return [None if is_prime(n) else first_divisor(n) for n in interpretations]


@memo
def first_divisor(n):
    ceil = int(sqrt(n))
    for candidate in xrange(2, ceil + 1):
        if n % candidate == 0:
            return candidate


to_base = int  # >>> to_base('100011', 2)  # 35


def fermat_primality_test(n, n_tests=1):
    # from https://gist.github.com/bnlucas/5857437
    # also see https://mitpress.mit.edu/sicp/chapter1/node17.html
    _test = lambda a: pow(a, n-1, n) == 1
    return any(_test(randint(1, n-1)) for _ in xrange(n_tests))


def fermat_alt(n):
    # from https://gist.github.com/bnlucas/5857437
    if n == 2:
        return True
    if not n & 1:
        return False
    return pow(2, n-1, n) == 1


def main():
    T = int(raw_input())
    for t in xrange(1, T+1):
        print 'Case #{}:'.format(t)

        N, J = map(int, raw_input().split())
        jamcoins = find_jamcoins(N, J)

        for jc in jamcoins:
            print '{} {}'.format(jc, ' '.join(map(str, divisors(jc))))
        # print '\n'.join('{} {}'.format(jc, ' '.join(str(d) for d in divisors(jc))) for jc in jamcoins)


if __name__ == '__main__':
    main()
