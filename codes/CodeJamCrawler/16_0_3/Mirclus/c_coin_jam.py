#! /usr/bin/env python3
import sys
import numpy as np
import random


def read_primes():
    with open('primes.dat', 'rb') as f:
        return np.fromfile(f, dtype=np.uint32)


def get_divisor(val, primes):
    for p in primes:
        if p >= val:
            return None
        if val % p == 0:
            return p

    return None


def c_coin_jam(length, count):
    primes = read_primes()

    print('Case #1:')
    sys.stdout.flush()

    solutions = []
    checked = []
    while len(solutions) < count:
        values = [1] * 9

        for i in range(length - 1):
            new_value = random.randint(0, 1)

            if i == length - 2:
                new_value = 1

            for mul in range(2, 11):
                values[mul-2] *= mul
                values[mul-2] += new_value

        if values[-1] in solutions or\
                values[-1] in checked:
            continue
        checked.append(values[-1])
        divisors = []
        for val in values:
            div = get_divisor(val, primes)
            if not div:
                break
            divisors.append(div)

        if len(divisors) < 9:
            continue

        solutions.append(values[-1])
        print("{} {}".format(
                values[-1],
                " ".join([str(x) for x in divisors])
                ))
        sys.stdout.flush()


def main():
    if len(sys.argv) < 3:
        print("Usage: {} length count".format(sys.argv[0]))
        sys.exit(1)
    c_coin_jam(int(sys.argv[1]), int(sys.argv[2]))


if __name__ == "__main__":
    main()
