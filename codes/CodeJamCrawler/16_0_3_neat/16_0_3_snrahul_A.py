from __future__ import print_function

import random;
import math;
from cmath import sqrt

t = input();


def prime(number):
    ''' if number != 1 '''
    if (number > 1):
        ''' repeat the test few times '''
        for time in xrange(12):
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = random.randint(2, number)-1
            
            ''' Test if a^(n-1) = 1 mod n '''
            if ( pow(randomNumber, number-1, number) != 1 ):
                return True
        return False
    
def perfectSquare(number):
    x = math.floor(math.sqrt(number))
    if x * x == number:
        return True
    else:
        return False
    
    

def findFactor(number):
    i = 2 
    while 1:
        if number % i == 0:
            return i;
        if i > int(sqrt(number).real) or i > 1e6:
            break 
        else:
            i += 1
    return number;
    
    
def conv_10(num,val):
    x = 0
    powval = 0
    for i in xrange(num):
        if ((val >> i) & 1):
            x += pow(10, powval)
        powval = powval + 1
    return x


def check(no, req, val):
    ans = 12 * [0];
    for i in range(2, 11, 1):
        x = 0;
        powval = 0;
        for j in xrange(no):
            if ((val >> j) & 1):
                x += pow(i, powval);
            powval= powval + 1
        y = prime(x);
        if (not y):
            return False;
        else:
            p = findFactor(x)
            if p == x:
                return False
            else:
                ans[i] = p;
    print("%d " %conv_10(no, val), end='');
    for i in range(2, 11, 1):
        print("%d " %ans[i], end='');
    print();
    return True

def solve(no, req):
    for i in xrange(1 << (no - 2)):
        x = 1
        for j in range(no - 2):
            if ((i >> j) & 1):
                x <<= 1;
                x += 1;
            else:
                x <<= 1;
        x <<= 1;
        x += 1;
        if(check(no, req, x)):
            req = req - 1
        if (req == 0):
            break;


for cases in range(1, t+1, 1):
    n, j = map(int, raw_input().split(' '));
    print('Case #%d:' %cases )
    solve(n, j)