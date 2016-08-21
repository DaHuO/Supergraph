import random
from collections import OrderedDict
import math
#from functools import reduce
#import operator


def print_for_data(length, number):
    potential_jamcoins = get_potential_jamcoins(length)
    random.shuffle(potential_jamcoins)
    
    #print(potential_jamcoins)   # Debug
    
    total = 0
    for pot_jc in potential_jamcoins:
        compute_current_pot_jc = interpret_potential_jamcoin(pot_jc)
        #print('* %s' % pot_jc)    # Debug
        
        values_divisors = OrderedDict()
        for i in range(2, 11):
            value = compute_current_pot_jc(i)
            #print('| %d' % value)    # Debug
            divisor = find_nontrivial_divisor(value)
            
            if divisor == None:
                break
            else:
                values_divisors[value] = divisor
        else:
            total += 1
            print(pot_jc, *values_divisors.values())
        
        if total >= number:
            break

def get_potential_jamcoins(length):
    return [bin(i)[2:]
            for i in range(2 ** (length - 1) + 1, 2 ** length + 1, 2)]

def interpret_potential_jamcoin(pot_jc):
    def compute_value(base):
        return sum(base ** i
                   for (i, c) in enumerate(reversed(pot_jc))
                   if c == '1')
    
    return compute_value

def find_nontrivial_divisor(num):
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            return i


# Because of this the program works VERY long
# (even for 14-length input it takes ~30 secs in average to complete)
'''
def find_nontrivial_divisor(num, max_prime_divisors):
    prime_divisors = []
    
    for i in primerange(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            prime_divisors.append(i)
        
        if len(prime_divisors) > max_prime_divisors:
            break
    
    if len(prime_divisors) == 0:
        return None
    
    constraint = min(max_prime_divisors, len(prime_divisors))
    constraint = constraint - 1 if constraint > 1 else constraint
    prime_divisors_count = random.randint(1, constraint)
    chosen_prime_divisors = random.sample(prime_divisors, prime_divisors_count)
    
    return reduce(operator.mul, chosen_prime_divisors, 1)

def primerange(begin, end):
    for i in range(begin, end):
        if is_prime(i):
            yield i

def is_prime(num):
    for n in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    
    return True
'''


def main():
    count = int(input())
    
    for i in range(count):
        length, number = [int(i_str) for i_str in input().split()]
        print('Case #%d:' % (i + 1))
        print_for_data(length, number)

if __name__ == '__main__':
    main()