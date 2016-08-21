import math


def is_prime(number):
    for x in xrange(2, int(math.sqrt(number)) + 1):
        if number % x == 0:
            return False, x
    return True, 0


def gen():
    primes = 0
    print "Case #1:"
    for i in xrange(16384):
        bini = bin(i)[2:]
        mask = '1' + '0' * (14 - len(bini)) + bini + '1'
        divs = []
        for base in xrange(2, 11):
            prime, div = is_prime(int(mask, base))
            if prime:
                break
            divs.append(div)
        else:
            print mask, ' '.join(map(str, divs))
            primes += 1
        if primes == 50:
            break


if __name__ == '__main__':
    gen()