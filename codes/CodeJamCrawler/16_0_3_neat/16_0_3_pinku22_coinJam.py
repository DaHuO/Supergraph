from math import sqrt; from itertools import count, islice
def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def factor(n):
    for i in range (2,int(sqrt(n)+1) ):
        if n%i==0:
            return i

def dofunc(bin_len,numbers):   
    c=1
    i=0
    numbers =10
    while i < (2**(bin_len-2))-1 and c<(numbers+1):
        a=bin(i)[2:]
        a=((bin_len-2)-len(a))*"0"+a
        number = "1"+a+"1"
        primality = True
        for base in range(2,11):
            if isPrime( int (number , base) ) :
                primality = False
                break       
        if primality == True:
            c=c+1
            pass
            print number,
            for base in range(2,11):
                print factor(int (number ,base)),
            print
        i=i+1
    
n=int(input())
ccc=1
while n:
    n=n-1
    aa=[int(i) for i in raw_input().split()]
    print "Case #%d:"%ccc
    dofunc(aa[0],aa[1])