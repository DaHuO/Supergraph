#Varun Bharadwaj

import itertools
from math import sqrt; from itertools import count, islice


def isNotPrime(n):
    #if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return number
    return False

'''def isNotPrime(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return i
        i = i+1
    return False'''

def check_jamcoin(n,base):
    '''res = [False]*9
    m = max(base)

    i=2
    b = base[:]
    while i*i<=m:
        for x in b:
            if i>x and not res[base.index(x)]:
                return []
            if x!=i:
                if x%i == 0:
                    res[base.index(x)] = i
                    b.remove(x)
        i = i+1
    
    if all(res):
        res.insert(0,n)
        return res
    else:
        return []'''
    res = []
    for x in base:
        r = isNotPrime(x)
        if not r:
            return False
        else:
            res.append(r)
    return [n]+res

def get_jamcoin(n,j):
    numcoins = 0
    
    for num in itertools.product([0,1],repeat=n-2):
        if numcoins < j:
            num = '1'+''.join(map(str,num))+'1'
            base = [] # num in base 2 to 10
            for i in range(2,11):
                base.append(int(num,i))
            res = check_jamcoin(num,base)
            if res:
                print(*res)
                numcoins = numcoins + 1
        else:
            return
        
        
testcases = int(input())
for tc in range(1,testcases+1):

    n,j = input().split()
    n = int(n)
    j = int(j)
    
    print('Case #',tc,':',sep='')
    get_jamcoin(n,j)




    
    

            
