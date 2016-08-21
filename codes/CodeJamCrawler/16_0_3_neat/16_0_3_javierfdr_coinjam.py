# Google Code Jam 2016
# javierfdr@gmail.com
# CoinJam

from random import *

# returns the list of numbers for each base that corroborate is jam coin or empty list otherwise
def is_jam_coin(number):
    nstr = str(number)
    if (nstr[0]!= '1' or nstr[len(nstr)-1] !='1'):
        return False

    primeBreakers = []
    for i in range(2,11):
        numInBase = convert(nstr,i,10)
        breaker = is_prime(int(numInBase))
        if (breaker == 0):
            return []
        else:
            primeBreakers.append(breaker)
    return primeBreakers

# taken from http://code.activestate.com/recipes/577944-random-binary-list/
randBinList = lambda n: ''.join([str(randint(0,1)) for b in range(1,n+1)])

def generate_j_jam_coins(num_size,total_coins):

    total_generated = 0
    result_list = {}

    while(total_generated < total_coins):
        coin = randBinList(num_size-2)
        coin = '1'+coin+'1'
        breakers = is_jam_coin(coin)
        if (breakers != []):
            result_list[coin] = breakers
            total_generated = len(result_list.keys())

    return result_list

# Maybe naive implementation but definitely practical since thousands of prime numbers have been generated
#def isPrime(number):



# The following 3 functions are taken from the elegant solution at
# https://www.quora.com/How-do-I-write-a-program-in-Python-that-can-convert-an-integer-from-one-base-to-another

def frm(x, b):
    """
    Converts given number x, from base 10 to base b
    x -- the number in base 10
    b -- base to convert
    """
    assert(x >= 0)
    assert(1< b < 37)
    r = ''
    import string
    while x > 0:
        r = string.printable[x % b] + r
        x //= b
    return r
def to(s, b):
    """
    Converts given number s, from base b to base 10
    s -- string representation of number
    b -- base of given number
    """
    assert(1 < b < 37)
    return int(s, b)
def convert(s, a, b):
    """
    Converts s from base a to base b
    """
    return frm(to(s, a), b)


#Very naive prime validator, that only checks until number 1500000. After that number outputs 0 saying is prime
# Outputs the number that corroborates is not prime
def is_prime(n):
    isPrimer = True
    maxCheck = 1500000
    if (n < maxCheck):
        maxCheck = n

    i = 2
    while (i<maxCheck):
        if n%i == 0:
            isPrimer = False
            return i
        i = i+1

    return 0

out_file = open('output.out','w+')
out_file.write('Case #1:'+'\n')

coins = generate_j_jam_coins(32,500)

for c in coins.keys():
    result = str(c) + ' '+ ' '.join([str(i) for i in coins[c]])+'\n'
    out_file.write(result)