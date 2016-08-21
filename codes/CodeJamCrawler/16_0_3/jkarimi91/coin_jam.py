
# coding: utf-8

# In[ ]:

from math import sqrt
from itertools import product

def is_jamcoin(coin):
    base = 2
    while base<=10:
        value = int(coin,base)
        if is_pseudoprime(value):
            return False
        base += 1
    return True

def is_pseudoprime(value):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
              59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
              127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
              191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
              263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349]
    for p in primes:
        if value%p == 0:
            return False
    return True
        
def get_nontrivial_divisors(jamcoin):
    divisors = []
    for base in xrange(2,10+1):
        value = int(jamcoin,base)
        for divisor in xrange(2,int(sqrt(value))+1):
            if value%divisor == 0:
                divisors.append(divisor)
                break
    return divisors
    
t = int(raw_input())
for case in xrange(1,t+1):
    n,j = map(int,raw_input().split())
    coins = product('01', repeat=n-2)
    num_of_jamcoins = 0
    jamcoins = []
    while num_of_jamcoins<j:
        coin = ''.join(coins.next())
        coin ='1'+str(coin)+'1'
        if is_jamcoin(coin):
            num_of_jamcoins += 1
            jamcoins.append(coin)
    
    print "Case #{}:".format(case)
    for jamcoin in jamcoins:
        divisors = get_nontrivial_divisors(jamcoin)
        divisors = ' '.join(map(str,divisors))
        print "{} {}".format(jamcoin,divisors)
        
        
            
        
            
                
        
        
    
        


# In[ ]:



