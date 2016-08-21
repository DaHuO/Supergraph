__author__ = 'gosu'

from math import sqrt

def get_coin(width):
    width = width - 2
    for val in range(2**width):
        yield '1' + bin(val)[2:].zfill(width) + '1'

def load_primes():
    primelist = []
    for line in open('10to8primes.txt'):
        primelist.append(int(line))
    def is_prime(n):
        for prime in primelist:
            if n % prime == 0:
                return prime
            if sqrt(n) <= prime:
                return 0
        return 0
    return is_prime

def main():
    inp = open("input.in")
    out = open("output", "w")
    c = int(inp.readline())
    vals = [int(x) for x in inp.readline().strip().split()]
    #n = vals[0]
    #j = vals[1]
    n = 32
    j = 500
    ## SMALL CASE
    is_prime = load_primes()

    coingen = get_coin(n)
    for x in range(2**30):
        coin = next(coingen)
        bases = [int(coin, x) for x in range(2, 11)]

        divisors = []
        for num in bases:
            divisor = is_prime(num)
            if divisor > 0:
                divisors.append(divisor)
            else:
                break
        if len(divisors) == 9:
            out.write(coin + ' ' +  ' '.join([str(x) for x in divisors]))
            out.write('\n')
            out.flush()
            print(coin + ' ' +  ' '.join([str(x) for x in divisors]))
        else:
            print('False: ' + coin)
        #print(bases)
    out.close()
    print("done")

if __name__ == '__main__':
    main()