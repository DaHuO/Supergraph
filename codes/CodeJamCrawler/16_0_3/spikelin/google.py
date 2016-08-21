# __author__ = 'xjlin'
# -*- coding: utf-8 -*-
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import random
import math
t = int(input())# read a line with a single integer
def create(n):
    pool = ['0' ,'1']
    str = '1'
    strbody = ''
    for i in range(n-2):
        strbody = strbody + random.choice(pool)
    return str + strbody + str
def isprime(n):
    if n <= 1:
        return n
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return i
        return -1
def interpret(n, base):
    flag = 0
    temp = 0
    while n != 0:
        temp += (n%10) * pow(base, flag)
        flag += 1
        n = n //10
    return temp
#print(interpret(100011, 3))
def isjamcoin(n):
    divisors = []
    for base in range(2, 11):
        temp = isprime(interpret(n, base))
        if temp == -1:
            break
        else:
            divisors.append(temp)
    return divisors

for i in range(1, t + 1):
    n, j = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    jampool = []
    print("Case #{}: ".format(i))
    while j >0:
        jamcoin = int(create(n))
        if jamcoin not in jampool:
            jampool.append(jamcoin)
            array = isjamcoin(jamcoin)
            if len(array) != 9:
                pass
            else:
                print(jamcoin, end='')
                for x in range(len(array)):
                    print(' '+ str(array[x]),end='')
                print('\n')
                j -= 1



    # check out .format's specification for more formatting options