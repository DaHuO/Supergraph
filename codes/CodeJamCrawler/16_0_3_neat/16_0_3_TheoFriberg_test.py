
from math import sqrt
import time

from itertools import chain, cycle, accumulate # last of which is Python 3 only


def isPrime(aaahahahahahaaa):
    canned = (2, 3, 5, 7, 11, 13, 19, 23, 27)
    for prime in canned:
        if aaahahahahahaaa < prime and aaahahahahahaaa % prime == 0:
            return aaahahahahahaaa
    i = 27
    end = sqrt(aaahahahahahaaa)#int(sqrt(aaahahahahahaaa))+2
    if(end >= aaahahahahahaaa):
        end = aaahahahahahaaa-1
    start = int(round(time.time() * 1000))
    while i < end:
        if aaahahahahahaaa % i == 0:
            return i
        i = i + 2
        if(int(round(time.time() * 1000)) - start > 100): # Give up if life is tough on you.
            return "True"
    return "True"

def isJamCoin(aaahahahahahaaa):
    stopCondition = True
    i=2
    factors = []
    while stopCondition and i < 11:
        data = isPrime(int(aaahahahahahaaa, i))
        stopCondition = not data == "True"
        if stopCondition:
            factors.append(str(data))
        i = i + 1
    return factors

coins = []
i = 0
while len(coins) < 500:
    f = isJamCoin("1"+bin(i)[2:].zfill(30)+"1")
    if(len(f) == 9):
        coins.append("1"+bin(i)[2:].zfill(30)+"1 "+" ".join(f))
    i = i + 1

print("Case #1:")
for line in coins:
    print(line)
