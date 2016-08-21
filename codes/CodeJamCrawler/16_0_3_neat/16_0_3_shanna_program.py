#!/usr/bin/python

from itertools import count, islice


def is_prime(n):
    if n < 2:
        return False
    for number in islice(count(2), int(n ** 0.5 - 1)):
        if not n % number:
            return number
    return True

def main():
    coins = []
    num = '1000000000000001'
    assert len(num) == 16
    while len(coins) != 50:
        divisors = []
        for i in range(2,11):
            result = is_prime(int(num, i))
            if result == True:
                break
            else:
                divisors.append(result)
        else:
            coins.append((num, [str(d) for d in divisors]))
        num = '{0:b}'.format(int(num, 2) + 2)
    assert len(coins) == 50
    print('Case #1:')
    for num, d in coins:
        print('{} {}'.format(num, ' '.join(d)))

if __name__ == '__main__':
    main()
