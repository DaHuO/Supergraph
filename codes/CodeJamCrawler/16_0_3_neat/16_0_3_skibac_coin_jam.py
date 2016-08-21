import sys
import math


def get_coins(n, j):
    coins = {}
    for number in coin_generator(n):
        base_interpretations = get_base_interpretations(number)

        divisors = []
        for base_interpretation in base_interpretations:
            divisor = get_nontrivial_divisor(base_interpretation)

            if not divisor:
                break

            divisors.append(divisor)

        else:
            coins[number] = divisors

            if len(coins.keys()) == j:
                return coins


def coin_generator(length):
    template = '1' + '0'*(length - 2) + '1'
    yield template
    template_value = int(template, 2)
    for number in xrange(2, pow(2, length-1)-1, 2):
        yield '{0:b}'.format(template_value + number)


def get_base_interpretations(number):
    return [int(str(number), base) for base in range(2, 11)]


def get_nontrivial_divisor(number):
    if number == 1:
        return False

    for n in xrange(2, int(math.sqrt(number) + 1)):
        if number % n == 0:
            return n

    return None


def main():
    test_cases_count = sys.stdin.readline().strip()

    for case_no in range(1, int(test_cases_count)+2):
        line = sys.stdin.readline().strip()

        if not line:
            continue

        n, j = line.split(' ')
        coins = get_coins(int(n), int(j))
        print 'Case #%s:' % case_no
        for coin, divisors in coins.iteritems():
            print '%s %s' % (coin, ' '.join([str(x) for x in divisors]))

if __name__ == '__main__':
    main()
