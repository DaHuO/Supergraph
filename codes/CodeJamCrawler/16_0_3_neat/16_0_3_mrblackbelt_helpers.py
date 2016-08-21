import itertools
from math import sqrt, floor


def get_primes(boundary):
    ranges = lambda stop: iter(itertools.count().next, stop)
    print zip(ranges, [True])
    exit()
    sieve = [True] * boundary 
    primes = xrange(2, int(boundary ** 0.5) + 1)
    for x in primes:
        if sieve[x]:
            for i in xrange(x + x, len(sieve), x):
                sieve[i] = False
    return [i for i in xrange(2, len(sieve)) if sieve[i]]

def is_prime(number):
    if number <= 2:
        return True
    start = 2
    mid = floor(sqrt(number)) + 1
    while start < mid: 
        if number % start == 0:
            return False
        start += 1
    return True


def number_to_base(num, base): 
    if num == 0:
        return [0] 
    if base == 10:
        return num
    numbers = [int(number) for number in str(num)]
    numbers.reverse()
    total = 0
    start = 1
    for number in numbers:
        if number:
            total += number * start
        start *= base
    return total


def generate_possible_jamcoins(length):
    length_minus_ends = length - 2
    return ['1{0}1'.format("".join(sequence)) for sequence in itertools.product("01", repeat=length_minus_ends)]


def get_all_divisors(number):
    mid = int(floor(sqrt(number))) + 1
    return [x for x in xrange(2, mid) if number % x == 0]

def get_first_divisor(number):
    start = 2
    while True:
        if number % start == 0:
            return start 
        start += 1
     
    
        


if __name__ == '__main__':
    #jamcoins =  generate_possible_jamcoins(6)
    jamcoins = ['1001']
    start, end = 2, 10
    for jamcoin in jamcoins:
        while start <= end:
            base_number = int(number_to_base(jamcoin, start))
            print base_number, get_all_divisors(base_number)
            start += 1
        

        
    
