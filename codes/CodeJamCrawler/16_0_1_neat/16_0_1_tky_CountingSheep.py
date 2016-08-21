# Google code jam counting sheep
import numpy

# awrward search for digits
def findDigits(N):
    flag = [0,0,0,0,0,0,0,0,0,0]
    if N > 0:
        n=0
        while(True):
            if 10**n>N:
                break
            n+=1

        n-=1
        while(n>=0):
            d = N//(10**n)
            flag[d]=flag[d]|1
            N = N%10**n            
            n-=1
    return(flag)

# quick and dirty element-wise OR for 10-element list
def addToFlags(a,b):
    for j in [0,1,2,3,4,5,6,7,8,9]:
        a[j] = a[j]|b[j]
    return(a)
        
T = int(input()) # read number of cases from stdin

for j in range(1,T+1):

    N = int(input()) # read a single integer per case

    # small dataset: 0 \leq N \leq 200
    # large dataset: 0 \leq N \leq 1e6

    M = N
    flags = findDigits(M)

    # only number that creates insomnia is zero
    while(M>0):
        M += N
        flags = addToFlags(flags,findDigits(M))
        if sum(flags) == 10:
            break
        
    if M==N:
        print("Case #{}: {}".format(j,'INSOMNIA'))
    else:
        print("Case #{}: {}".format(j,M))
        
