# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 13:29:09 2016

@author: M
"""
import random as rnd
from math import ceil

#prime number generator based on stackoverflow
def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def test_jamcoin(jamcoin):
    divisor_list = []
    for base in xrange(2,11):
        jam_num = int(jamcoin,base)
        jam_num_sqrt = ceil(jam_num**0.5)
        found = False
        for i in prime_list:
            if i> jam_num_sqrt:
                return None
            if jam_num % i == 0:
                divisor_list.append(i)
                found = True
                break
        if found == False:
            return None
    return divisor_list



output_path = r'C:\Users\M\Documents\Python\ocde jam 2016\q3\C_large.out'
output_file = open(output_path,'w')
output_file.write('Case #1:\n')

len_jamcoin = 32
num_jamcoin = 500
jamcoin_preset = 2**(len_jamcoin-1) +1
jamcoins = []

if 'prime_list' not in vars():
    prime_list = primes(10**8)



while len(jamcoins)<num_jamcoin:
    new_jamcoin = bin(jamcoin_preset | (rnd.getrandbits(len_jamcoin-2)<<1))[2:]
    divisors = test_jamcoin(new_jamcoin)
    if divisors and (new_jamcoin not in jamcoins):
        jamcoins.append(new_jamcoin)
        print len(jamcoins), new_jamcoin, divisors
        output_file.write(new_jamcoin + ' ' + str(divisors)[1:-1].replace(',','') + '\n')
        
print 'fin'
output_file.close()








    
    
