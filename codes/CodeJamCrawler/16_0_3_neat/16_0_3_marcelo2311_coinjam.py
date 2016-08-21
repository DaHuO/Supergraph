from math import sqrt; from itertools import count, islice
def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

_T = readint()

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def convert(N, b):
    ma = len(N)
    
    r = 0
    for i in range(ma):
        r = r + (int(N[i])*b**(ma-i-1))
    #print r
    return r

def getList(D, m):
    l = []
    l.append(1)
    for j in range(D-2):
        l.append(m)
    l.append(1)
    return l      

def getNonTrivialDivisor(N, L):
    for i in range(3, N-1):
        if(N%i == 0 and i not in L):
            return i

for _t in range(_T):
    D,J = raw_input().split()
    
    mi = getList(int(D), 0)
    ma = getList(int(D), 1)
    r = []
    
    print 'Case #%i:'%(_t+1)
    for i in range(convert(mi, 2),convert(ma, 2)+1 ):
        if(i%2 != 0):
            string = "{0:b}".format(i)
            #print string
            valid = True
            L = []
            P = []
            for j in range(2, 11):
                nb = convert(list(string), j)
                L.append(getNonTrivialDivisor(nb, L))
                P.append(nb)
                if(isPrime(nb)== True):
                    #print nb
                    valid = False
                    break
            if(valid):
                r.append(string)
                if(len(r)<=int(J)):
                    print string, " ".join(str(x) for x in L)
                    print string, " ".join(str(x) for x in P)
                else:
                    break        
            
        
        
    #print isPrime(convert([1,0,1], 2))
   
   

    #print 'Case #%i:'%(_t+1), j
