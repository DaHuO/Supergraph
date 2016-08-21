import math


def nextNumber(num):
    n = len(num)
    i = n-2
    carry = 1
    newNum = ""
    while i >= 1:
        carry += int(num[i])
        newNum += str(carry % 2)
        carry //= 2
        i -= 1
    return "1" + newNum[::-1] + "1"


def getAnyDivisor(num):
    limit = int(math.sqrt(num)+2)
    for i in range(2, limit):
        if num % i == 0:
            return i
    return 0


input()
lal = input().split(" ")
print("Case #1:")
N = int(lal[0])
J = int(lal[1])
number = ''.join(['1' if x == 0 or x == N-1 else '0' for x in range(N)])
i = 0
lim_i = 1 << N-2
while i < lim_i and J > 0:
    divs = list()
    for base in range(2, 11):
        n = int(number, base)
        divs.append(getAnyDivisor(n))
        if not divs[-1]:
            break
    else:
        print(number, end='')
        for x in divs:
            print(' '+str(x), end='')
        print("")
        J -= 1
    number = nextNumber(number)
    i += 1
