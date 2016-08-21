import sys
import math
    
s = sys.stdin
t = int(s.readline())
line = s.readline().split()
N = int(line[0])
J = int(line[1])

jamcoin = [0] * N
jamcoin[0] = 1
jamcoin[N - 1] = 1

numCompleted = 0
numPossibilities = 2**(N-2)

print("Case #1:")
for i in range (numPossibilities):

    currentNum = i
    divisors = []
    for j in range(1, N-1):
        jamcoin[N - j - 1] = currentNum % 2
        currentNum = currentNum / 2

    completed = True
    for base in range(2, 11):
        value = 0
        multiplier = 1
        for j in range(N):
            value = value + jamcoin[N - j - 1] * multiplier
            multiplier = multiplier * base

        # Check for primality
        root = math.sqrt(value)
        prime = True
        for divisor in range(2,int(root) + 1):
            if (value % (divisor) == 0):
                divisors.append(divisor)
                prime = False
                break
        
        if (prime):
            completed = False
            break
    if (completed):
        print(''.join(str(x) for x in jamcoin) + ' ' + ' '.join(str(x) for x in divisors))
        
        numCompleted = numCompleted + 1
    if (numCompleted == J):
        break

