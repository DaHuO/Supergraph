# -*- coding: utf-8 -*-
"""
/**********************************************************************************************
* Sometimes it is the people no one imagines anything of who do the things no one can imagine.*
*                                                                                             *
*                                    User: LLcoolNJ                                           *
***********************************************************************************************/
"""
import sys
inp = sys.stdin.readline

def getInt():
    return int(inp().strip())
    
def getList():
    return map(int, inp().strip().split())

def getStr():
    return inp().strip()


def isPrime(x):
    primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29,31, 37, 41, 43, 47, 53, 59, 61, 67, 71,73, 79, 83, 89, 97, 101, 103, 107, 109, 113,127, 131, 137, 139, 149, 151, 157, 163, 167, 173,179, 181, 191, 193, 197, 199, 211, 223, 227, 229,233, 239, 241, 251, 257, 263, 269, 271, 277, 281,283, 293, 307, 311, 313, 317, 331, 337, 347, 349,353, 359, 367, 373, 379, 383, 389, 397, 401, 409,419, 421, 431, 433, 439, 443, 449, 457, 461, 463,467, 479, 487, 491, 499, 503, 509, 521, 523, 541,547, 557, 563, 569, 571, 577, 587, 593, 599, 601,607, 613, 617, 619, 631, 641, 643, 647, 653, 659,661, 673, 677, 683, 691, 701, 709, 719, 727, 733,739, 743, 751, 757, 761, 769, 773, 787, 797, 809,811, 821, 823, 827, 829, 839, 853, 857, 859, 863,877, 881, 883, 887, 907, 911, 919, 929, 937, 941,947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013]
    for num in primes:
        if x % num == 0 and x != num:
            return [False, num]
    return [True]

"""def isPrime(num):
    if num < 2: 
        return [False]
    if num == 2 or num == 3: 
        return True
    if num % 2 == 0:
        return [False, 2] 
    if num % 3 == 0:
        return [False, 3]    
    maxDivisor = num**0.5
    d, i = 5, 2
    while d <= maxDivisor:
        if num % d == 0: 
            return [False, d]
        d += i 
        i = 6 - i
    return [True]"""
def check(num):
    nums = []
    for i in xrange(2, 10):
        n = int(num, i)
        r = isPrime(n)
        #print n, i, r
        if len(r) == 1:
            return False
        nums.append(str(r[1]))
        
    r = isPrime(int(num))
    if len(r) == 1:
        return False
    nums.append(str(r[1]))
    return nums

T = getInt()
#### Foo Small Dataset
for cs in xrange(1, T+1):
    print "Case #%d:" %(cs)
    N, J = getList()
    cnt = 0
    i = 0
    req = N-2
    while cnt < J:
        s = list(bin(i)[2:])
        s = ['0']*(req - len(s)) + s
        num = ['1'] + s + ['1']
        if len(num) != N:
            break
        flag = check(''.join(num))
        #print ''.join(num)
        if flag:
            cnt += 1
            print ''.join(num), ' '.join(flag)
        i += 1