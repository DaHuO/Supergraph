import math

def aTD(n, base):
    m = 0
    i = 1
    while n != 0:
        m += (n % 10)*i
        n = n // 10
        i *= base
    return m

def decToBin(n):
    return str(bin(n))[2:]

def isPrime(a):
    i = 2
    while i < (53):
        if a % i == 0:
            return i
        i += 1
    return -1

primon = ""


def ifPrimeInAllBases(n):
    global primon
    primon = ""
    for i in range(2,11):
        kol = isPrime(aTD(n,i))
        if kol == -1:
            return False
        primon += ' ' + str(kol)
    return True

m = int(input())
for l in range(1,m+1):
    n,j = input().split()
    n = int(n)
    j = int(j)
    print("Case #",l,":", sep='')
    for i in range(2**(n-1)+1, 2**(n),2):
        if j == 0:
            break

        bina = decToBin(i)
        da = int(bina)
        if ifPrimeInAllBases(da) == True:
            j -= 1
            print(bina,primon, sep='')
