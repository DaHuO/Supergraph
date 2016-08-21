"""
Author: Sam Vitello
CodeJam 2016 Qualifying Round
CoinJam
"""

import itertools


def primes_generator():
    """
    generator that yields primes based on Sieve of Eratosthenes
    """
    numbers = itertools.count(2)
    while True:
        prime = next(numbers)
        numbers = (lambda prime: (i for i in numbers if i % prime))(prime)
        yield prime


def test_num_for_base(t, base):
    num = 0
    tstring = t[::-1]
    for i, dig in enumerate(tstring):
        if dig == "1":
            num += base**i
    return num


def test_case_generator(lgth):
    test_lgth = lgth - 2
    gen = itertools.product([0,1], repeat=test_lgth)
    while True:
        middle = ""
        for c in next(gen):
            middle += str(c)
        yield "1" + middle + "1"


def get_coin_jams(str_lgth, t):
    jams = []
    g = test_case_generator(str_lgth)
    for case in g:

        divisors = []
        for i in range(2, 11):
            found = False
            t_num = test_num_for_base(case, i)

            p = primes_generator()

            # check first 50 primes for divisor
            for _ in xrange(50):
                t_prime = p.next()
                if t_num % t_prime == 0:
                    divisors.append(t_prime)
                    found = True
                    break

            if not found:
                break

        if len(divisors) == 9:
            jams.append((case, divisors))

        if len(jams) == t:
            return jams

    raise ValueError("Not enough CoinJams for target %d" % t)


def print_answer(answer_list):
    print "Case #1:"
    for cj, divs in answer_list:
        s = ""
        for div in divs:
            s += " "
            s += str(div)
        print cj + s


if __name__ == "__main__":
    iterations = int(raw_input())
    str_lgth, target = raw_input().split(" ")

    str_lgth = int(str_lgth)
    target = int(target)

    coin_jams = get_coin_jams(str_lgth, target)
    print_answer(coin_jams)








