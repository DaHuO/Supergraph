import sys
import copy
#sys.setrecursionlimit(1500)
from operator import itemgetter

def flipList(pancakes, position):
    # is it faster to do this?
    # ->just not all first position entries?
    for p in range(0,position+1):
        pancakes[p] = not pancakes[p]
    # or this?
    return pancakes#[pancakes[:position][::-1]:pancakes[position:]]
#

def calculate(stack):
    # convert N to a boolean list
    pancakes = []
    for p in stack:
        if p == '+':
            pancakes.append(True)
        else:
            pancakes.append(False)
    # I thnk that essentially what we want to do is
    # work from the bottom to the top.  So we have to keep flipping as far down as we can such that below the
    # flip there are only happy pancakes
    flipcount = 0
    lastknown = len(pancakes)-1
    while not all(pancakes):
        # iterate backwards through the list until there is a False
        # actually, only have to start from last known position.
        #position = len(pancakes)
        for p in range(lastknown, -1, -1):
            if pancakes[p] == False:
                #flip here
                pancakes = flipList(pancakes, p)
                flipcount+=1
                lastknown = copy.deepcopy(p)
                p = -1
                break
            
        
    return flipcount
        
infile = open(sys.argv[1],'r')

numcases = int(infile.readline().strip())
outfile = open(sys.argv[1].replace('.in','.out'),'w')
for n in range(numcases):
    stack = infile.readline().strip()
    
    flips = calculate(stack)
    
    
    ans = str(flips)# if flips != -1 else 'INSOMNIA'
    outfile.write("Case #" + str(n+1)+": " + ans + '\n')
    print ans

outfile.close()
