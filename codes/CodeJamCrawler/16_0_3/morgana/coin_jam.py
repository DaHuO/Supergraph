__author__ = 'morgana'

from math import pow, sqrt, ceil


def get_jam_coins(length, required_count):

    jam_coins = dict()

    max_num = int(pow(2, length))
    start_num = int(pow(2, length-1)) + 1
    for num in range(start_num, max_num):
        binary = bin(num)[2:]
        # use only numbers that start and end with 1
        if binary[:1] == '1' and binary[len(binary)-1:] == '1':

            # check if base numbers are not prime
            base_divisors = list()
            no_primes = True
            for base in range(2, 11):
                base_number = int(binary, base)
                divisor = get_divisor(base_number)
                if divisor:
                    base_divisors.append(divisor)
                else:
                    no_primes = False
                    break
            if no_primes:
                jam_coins[binary] = base_divisors
                print binary
        if len(jam_coins.keys()) == required_count:
            break

    return jam_coins


def get_divisor(num):
    for i in range(2, int(sqrt(num))):
        if not num % i:
            return i


if __name__ == '__main__':
    f = open('sample.txt')
    case_count = int(f.readline())

    cases = list()
    g = open('out.txt', 'w')
    for case_number in xrange(case_count):
        binary_length, required = f.readline().split(' ')
        g.writelines('Case #{}:\n'.format(case_number+1))
        jamcoins = get_jam_coins(int(binary_length), int(required))
        for jamcoin, divisors in jamcoins.items():
            g.writelines('{} {}\n'.format(jamcoin, ' '.join(str(divisor) for divisor in divisors)))
    g.close()
    f.close()