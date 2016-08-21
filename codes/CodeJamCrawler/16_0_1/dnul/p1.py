__author__ = 'dnul'

import math

def getDigits(n):
    digits=set()
    while(n>0):
        digits.add(n%10)
        if len(digits)==10:
            return digits
        n=n/10


    return digits

def solve(n):
    i=1
    digits=getDigits(n)
    if(n==0):
        return "INSOMNIA"

    while(len(digits)<10):
       i+=1
       number=i*n
       digits=digits.union(getDigits(number))

    return number




def main():
    f=open('input.txt','r')
    testcases=f.readline()
    for i in range(int(testcases)):
        N=f.readline().strip('\n')
        print 'Case #'+str(i+1)+': ' + str(solve(int(N)))




main()
