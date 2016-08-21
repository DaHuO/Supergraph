#!/usr/bin/env python3
import pickle
import os
import sys
import itertools
from functools import partial
from operator import mod


primes_cache = [2, 3]
divisor_cache = {2: None, 3: None}


def primes():
    yield from primes_cache
    for number in itertools.count(primes_cache[-1] + 2, 2):
        check = partial(mod, number)
        if all(map(check, primes_cache)):
            primes_cache.append(number)
            divisor_cache[number] = None
            yield number


def some_divisor(number):
    limit = number / 2 + 1
    for divisor in itertools.islice(primes(), 0, 1000):
        if divisor > limit:
            break
        elif number % divisor == 0:
            return divisor
    return None


def doit_generator(size, divisor_fn):
    assert size > 2
    template = '1{{:0{}b}}1'.format(size - 2)
    iteration_count = int(2 ** (size - 2))
    for iteration in range(iteration_count):
        if iteration % 10 == 0:
            sys.stderr.write(
                'Total progress: {} / {} ({:.2f})\n'.format(
                    iteration, iteration_count,
                    100.0 * iteration / iteration_count,
                )
            )
        result = template.format(iteration)
        divisors = []
        for base in range(2, 11):
            number = int(result, base)
            divisor = divisor_fn(number)
            if divisor:
                divisors.append(divisor)
            else:
                break
        else:
            sys.stderr.write('Found one jamcoin: {}\n'.format(result))
            yield (result, tuple(divisors))


def main():
    try:
        with open('primes.pickle', 'rb') as f:
            cache = pickle.load(f)
    except EnvironmentError:
        pass
    else:
        divisor_cache.update(cache)
        sys.stderr.write('Loaded divisor cache: {}\n'.format(len(divisor_cache)))

    try:
        assert sys.stdin.readline().strip() == '1'
        size, count = sys.stdin.readline().strip().split()
        sys.stdout.write('Case #1:\n')
        for _, (result, divisors) in zip(
                range(int(count)),
                doit_generator(int(size), some_divisor),
        ):
            sys.stdout.write(' '.join(itertools.chain(
                [result], map(str, divisors),
            )))
            sys.stdout.write('\n')
    finally:
        with open('primes.pickle.tmp', 'wb') as f:
            cache = pickle.dump(divisor_cache, f)
        os.rename('primes.pickle.tmp', 'primes.pickle')
        sys.stderr.write('Dumped divisor cache: {}\n'.format(len(divisor_cache)))


if __name__ == '__main__':
    main()
