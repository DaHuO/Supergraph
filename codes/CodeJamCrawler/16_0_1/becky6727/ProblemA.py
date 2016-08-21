import os, sys, time
import numpy
from collections import Counter

#FileIN = './Input/A-small-attempt1.in.txt'
FileIN = './Input/A-large.in.txt'

#index for Line number
N = 0

#array for test case
TestCase = []

for Lines in open(FileIN):

    #strip \n
    Line = Lines.rstrip('\n')

    #split lists with space
    Line = Line.split(' ')

    #type conversion
    for i in range(len(Line)):
        Line[i] = int(Line[i])
        pass
    
    if(N != 0):
        TestCase.append(Line[0])
    else:
        NofCase = int(Line[0])
        pass

    N += 1
    pass

tmp = Counter()

#count numbers
for i in range(NofCase):
    
    Num = TestCase[i]
    
    if(Num == 0):
        print 'Case #%d: INSOMNIA' %(i + 1)
        continue

    #initialize
    tmp.clear()

    kc = 2
    tmpNum = Num
    
    while(True):
        
        tmp += Counter(str(tmpNum))
                
        if(len(list(tmp)) == 10):
            break
        
        tmpNum = kc* Num
        tmpNum = int(tmpNum)
        kc += 1
        
        pass

    print 'Case #%d: %d' %(i + 1, tmpNum)
    
    pass
