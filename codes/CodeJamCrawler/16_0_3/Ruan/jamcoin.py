# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 10:58:58 2016

@author: theronrp
"""
import math
#f = open('small2.in')
fo = open('output.out', 'w')
fo.write('Case #1:\n')
N = 30
J = 500

def dec_to_bin(x):
    return bin(x)[2:]
    
def str_to_int_base_n(string, n):
    charList = list(string)
    result = 0
    for i in range(0, len(charList)):
        result = result + int(charList[i])*(n**(len(charList) - 1 - i))
    return result
    
def is_prime(n):
    if n <= 1:
        return -1
    elif n <= 3 :
        return n
    elif (n % 2) == 0 :
        return 2
    elif (n % 3) == 0:
        return 3
    i = 5
    while i <= (math.sqrt(math.sqrt(math.sqrt(n)))):
        if (n % i) == 0:
            return i
        elif (n % (i + 2)) == 0:
            return i + 2
        i += 6
    return -1

jamcoinCount = 0
counter = 2147483648 + 1
upperBound = 4294967296
#for jamcoin in range(2**(N-1) + 1, 2**N, 2) :
while counter < upperBound:
    jamcoinString = dec_to_bin(counter)
    
    baseDivs = [0] * 9    
    for n in range(2,11):
        jamcoinBaseN = str_to_int_base_n(jamcoinString, n)
        """isPrime = True
        print 'Checking base ' + str(n) + 'for prime'
        for i in range(2, int(math.sqrt(jamcoinBaseN)) + 1):
        #for i in range(2, jamcoinBaseN / 2):
            #if not is_prime(jamcoinBaseN):
            if jamcoinBaseN % i == 0:
                isPrime = False
                baseDivs[n - 2] = str(i)
                break"""
        #print 'Checking base ' + str(n) + 'for prime'
        posDiv = is_prime(jamcoinBaseN)
        isPrime = (posDiv == -1)
        if not isPrime :
            baseDivs[n - 2] = str(posDiv)
        else :
            break
        
    if not isPrime:
        print len(jamcoinString)
        print jamcoinString + " " + ' '.join(baseDivs)
        fo.write(jamcoinString + " " + ' '.join(baseDivs) + '\n')
        jamcoinCount += 1
        #print jamcoinString + ' is a prime in one of the bases'
    
    if jamcoinCount == J:
        break
    counter += 2
        
    
print str(jamcoinCount) + ' jamcoins found'
    
fo.close()