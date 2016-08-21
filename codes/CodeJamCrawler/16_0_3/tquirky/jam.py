#CODEJAM BABY
from random import randint
from math import sqrt
from itertools import count, islice
import itertools
flatten_iter = itertools.chain.from_iterable
outputStr = ""
problemFile = "example.txt"

def readF(fname):
    file = open(fname)
    file = file.read().split('\n')
    return file

def writeF(text):
    print(text)
    f = open('file.txt', 'w')
    f.write(text)

data = readF(problemFile)[1].split(' ')



def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def fac(n):
    return list(flatten_iter((i, n//i)
                for i in range(1, int(n**0.5)+1) if n % i == 0))

def gen(length):
    number = ""
    for i in range(length):
        number += str(randint(0, 1))

    return "1" + number[1:-1] + "1"

def jam(length, coins):
    bases = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    coinList = []
    coin_raw = []

    while len(coinList) < coins:
        print(len(coin_raw))
        success = []
        num = gen(length)[::-1]
        divisors = []
        for base in bases:
            places = [base ** i for i in range(length)]

            resolved_num = 0

            for digit in enumerate(num):
                resolved_num += places[digit[0]] * int(digit[1])
            if isPrime(resolved_num):
                success.append(False)
            else:
                factors = fac(resolved_num)
                for factor in factors:
                    if factor != 1 and factor != resolved_num:
                        divisors.append(str(factor))
                        break

                success.append(True)
        if False not in success:
            if num[::-1] not in coin_raw:
                print(divisors)
                coin_raw.append(num[::-1])
                coinList.append({num[::-1]: divisors})

    return coinList

coins = jam(int(data[0]), int(data[1]))
outputStr = "Case #1:\n"
for coin in coins:
    for num in coin:
        factor = " ".join(coin[num])
        outputStr += "%s %s\n" % (num, factor)
print(outputStr)

