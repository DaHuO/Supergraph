#!/usr/bin/env python


def is_prime(n):
    """ http://stackoverflow.com/a/1801446/83369 """
    if n == 2:
        return True, None
    if n == 3:
        return True, None
    if n % 2 == 0:
        return False, 2
    if n % 3 == 0:
        return False, 3
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False, i
        i += w
        w = 6 - w
    return True, None


def jammin(length, number):
    results = []
    for jc in [bin(x)[2:].rjust(length - 2, '0') for x in range(2 ** length - 2)]:
        jamcoin = '1' + jc + '1'
        divisors = []
        for base in range(2, 11):
            base_interpretation = int(jamcoin, base)
            prime_p, divisor = is_prime(base_interpretation)
            if prime_p:
                break
            else:
                divisors.append(divisor)
        else:
            results.append(tuple((jamcoin, divisors,)))
        if len(results) >= number:
            break
    return results


def main():
    num_cases = int(raw_input())
    for i in range(num_cases):
        length, number = raw_input().split()
        print('Case #{0}:'.format(i + 1))
        jamcoins = jammin(int(length), int(number))
        for jamcoin, divisors in jamcoins:
            print jamcoin + ' ' + ' '.join(map(str, divisors))

if __name__ == '__main__':
    main()
