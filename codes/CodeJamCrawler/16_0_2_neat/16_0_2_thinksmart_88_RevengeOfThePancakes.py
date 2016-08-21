'''
Created on Apr 9, 2016

@author: Ibrahim
'''

def count (pancakes):
    flips = 0
    i =0
    flipTogether = False 
    while True:
        if i>=len(pancakes):
            return flips
        
        if pancakes[i]=='+':       
            flipTogether  = True
            i=i+1
            
        else:
            if flipTogether:
                flips = flips + 2
            else:
                flips = flips + 1
            flipTogether = False
            while True:
                i=i+1
                if i>=len(pancakes):
                    return flips
                
                if (pancakes[i]=='-'):
                    continue
                else:
                    break
        
        
    return flips
            
'''
Driver code
'''
f = open('B-large.in','r')
outf = open ('large.out','w')
T = int(f.readline())

for i in xrange(0,T):
    pancakes = f.readline().rstrip()
    answer = count(pancakes)
    print 'Case #'+str(i+1)+': '+str(answer)
    outf.write('Case #'+str(i+1)+': '+str(answer)+'\n')
