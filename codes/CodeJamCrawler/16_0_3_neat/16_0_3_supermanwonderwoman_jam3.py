import random
from math import sqrt
from itertools import count, islice

def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), 9999999):
        if not n%number:
            return number
    return False

jamcoins = []

def coin_tester(num):
    divisors = []
    multipliers = [31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
    for x in range(2,11):
        digits = str(num)
        basex = 0
        for digit in range(0,32):
            basex += (int(digits[digit])*(x**multipliers[digit]))
        primers = isPrime(basex)
        if primers != False:
            divisors.append(primers)
        else:
            return False
    return divisors

def jamcoin_generator():
    print("Case #1:")
    jam = ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','0','1','0','1','0','1','0','1','0','1','1','1','1']
    while len(jamcoins) < 500:
        for x in range(1,31):
            jam[x] = str(random.randint(0,1))
        generated = int("".join(jam))
        if generated not in jamcoins:
            savejam = coin_tester(generated)
            if savejam != False:
                jamcoins.append(generated)
                print(generated, end="")
                for x in savejam:
                    print("",x, end="")
                print()
    

    
    
    

