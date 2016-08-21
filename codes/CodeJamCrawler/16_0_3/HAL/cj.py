'''
Created on Apr 9, 2016

@author: roadkill
'''

import itertools
from math import sqrt

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step
        
def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))
        
def get_valid_divisor(val):
    if is_prime(val):
        return False
    
    for i in itertools.count(1):
        if i == 1:
            continue
        if val % i == 0 and i != val and i != 1:
            return i
        if i == val + 1:
            break
    return False

def is_jamcoin(coin):
    divisors = []
    
    for base in range(2,11):
        val = int(coin, base)
        p = get_valid_divisor(val)
        if not p:
            return None
        divisors.append(p)
    
    if len(divisors) > 0:
        return divisors
    else:
        return None
    
def solve(coin_length, num_coins):
    res = []
    it = 0
    
    while not len(res) == num_coins:
        iter_str = format(it, "0" + str(coin_length - 2) + "b") 
        if(coin_length < 3):
            iter_str = ""
        current_coin = "1" + iter_str +"1"
        if len(current_coin) > coin_length:
            print "not enough solutions found"
            break
        
        #print "%d: %s" % (it, current_coin)
 
        ret = is_jamcoin(current_coin)
        
        if ret:
            res.append([current_coin] + ret)
    
        it += 1
        
    return res

for case in xrange(input()):
    N, J = [int(c) for c in raw_input().split()]
    
    res = solve(N, J)

    print "Case #%i:" % (case+1)
    for r in res:
        print " ".join(str(e) for e in r)