import math
t = input()

def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True

def FindAllDivisors(arr):
    divList = []
    for x in arr:
        y = 2
        while y <= math.sqrt(x):
            if x % y == 0:
                divList.append(y)
                break
            y += 1
    return divList

for i in range(t):
    n, limit = map(int, raw_input().split())
    count = 0
    print "Case #"+str(i+1)+": "
    for j in range(2**(n-2)):
        if count != limit:
            flag = True
            arr = [int('1'+bin(j)[2:].zfill(n-2)+'1',k) for k in range(2,11)]
            for l in arr:
                if isPrime2(l):
                    flag = False
                    break
            if flag:
                print '1'+bin(j)[2:].zfill(n-2)+'1', ' '.join(map(str, FindAllDivisors(arr)))
                count += 1