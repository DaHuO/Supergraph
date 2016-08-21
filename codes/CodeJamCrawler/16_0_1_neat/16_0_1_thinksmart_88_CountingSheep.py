'''
Created on Apr 9, 2016

@author: Ibrahim
'''
from sets import Set

def getDigits(number):
    return list(str(number))

def count(N):
    if N==0:
        return 'INSOMNIA'
    
    allDigits = Set(range(0,10))
    seen = Set([])
    current = N
    while True:
        digits = getDigits(current)
        for d in digits:
            seen.add(int(d))
        if seen.issuperset(allDigits):
            return current
        else:
            current = current + N

'''
Driver code
'''
f = open('A-large.in','r')
outf = open ('large.out','w')
T = int(f.readline())

for i in xrange(0,T):
    N = int(f.readline())
    answer = count(N)
    print 'Case #'+str(i+1)+': '+str(answer)
    outf.write('Case #'+str(i+1)+': '+str(answer)+'\n')
