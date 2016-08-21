import math
def isPrime(n):
    if n%2 == 0 and n > 2:
        return (False, 2)
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i == 0:
            return (False, i)
    return (True, 0)

def convertToBase(n, b):
    num = 0
    p = 1
    while n > 0:
        if n % 2 == 1:
            num += p
        n = int(n/2)
        p *= b
    return num


fo = open('C-small-attempt0.out', 'w')
fo.write('Case #1:\n')
N = 16
J = 50
for i in range(2**(N-1)+1, 2**(N), 2):
    found = True
    if isPrime(convertToBase(i, 10))[0]:
        continue
    for base in range(2, 10):
        num = convertToBase(i, base)
        if isPrime(num)[0]:
            found = False
            break
    if found:
        fo.write(bin(i)[2:])
        for base in range(2, 11):
            num = convertToBase(i, base)
            r = isPrime(num)
            fo.write(' '+str(r[1]))
        fo.write('\n')
        J -= 1
        print(J)
        if J == 0:
            break;