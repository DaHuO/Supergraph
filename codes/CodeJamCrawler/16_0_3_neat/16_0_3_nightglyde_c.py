import sys
import itertools
import math

limit = 1000

def checkPrime(n):
    for x in itertools.islice(itertools.count(2), min(int(math.sqrt(n)-1), limit)):
        if n % x == 0:
            return x
    return -1

cin = sys.stdin.readlines()
print("Case #{}:".format(cin[0].strip()))
N, J = [int(i) for i in cin[1].strip().split()]

coins = 0
for i in range(2**(N-1)+1, 2**N, 2):
    jamcoin = bin(i)[2:]
    divisors = []
    for base in range(2, 11):
        jamcoinB = int(jamcoin, base)
        divisor = checkPrime(jamcoinB)
        if divisor == -1:
            break
        divisors.append(divisor)
    else:
        print(jamcoin, *divisors)
        coins += 1
        if coins == J:
            break

