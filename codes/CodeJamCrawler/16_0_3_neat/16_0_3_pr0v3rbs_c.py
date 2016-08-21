import math

powerArr = [[],[],[],[],[],[],[],[],[],[],[]]
baseArr = [0,0,0,0,0,0,0,0,0,0,0]
jamArr = [0,0,0,0,0,0,0,0,0,0,0]
input()
N, J = raw_input().split()
N = int(N)
J = int(J)

def JamCheck():
    result = True
    idx = 0
    t = baseArr[2]

    for i in range(3, 11):
        baseArr[i] = 0

    while t != 0:
        if t % 2 == 1:
            for i in range(3, 11):
                baseArr[i] += powerArr[i][idx]
        idx += 1
        t /= 2

    for i in range(2, 11):
        primeCheck = True
        j = 2
        length = int(math.sqrt(baseArr[i])) + 1
        while j <= 10000:
            if baseArr[i] % j == 0:
                #jamArr[i] = j
                jamArr[i] = baseArr[i] / j
                primeCheck = False
                break
            j+=1
        if primeCheck:
            result = False
            break

    return result

def PrintJam():
    print bin(baseArr[2])[2:], jamArr[2], jamArr[3], jamArr[4], jamArr[5], jamArr[6], jamArr[7], jamArr[8], jamArr[9], jamArr[10]

for i in range(2, 11):
    for j in range(N):
        powerArr[i].append(i**j)


baseArr[2] = 2**(N-1) + 1

print "Case #1:"

while J != 0:
    if JamCheck() :
        PrintJam()
        J -= 1
    baseArr[2] += 2
