import math

def prime(s):
    if s % 2 == 0:
        return 2
    sqrtS = math.floor(math.sqrt(s))
    for k in range(3, sqrtS+1):
        if s % k == 0:
            return k
    return s

N = 16 #32
J = 50 #500

print('Case #1:')

halfN = int(N/2)
primeList = []
for i in range(2, 11):
    s = i**halfN + 1
    primeList.append(prime(s))
primeList = ' '.join(map(str, primeList))

for i in range(J):
    halfList = bin(2**(halfN-2)+i)[2:] + '1'
    print(halfList*2, primeList)
