import sys
import copy
#sys.setrecursionlimit(1500)
from operator import itemgetter

def calculate(N):
    # convert c_i_str into ints and binary
    found = []
    for f in range(10):
        found.append(False)
    # is it faster to use a dictionary?
    #found = {'0':False, '1':False, '2':False, '3':False, '3':False, '3':False, '3':False, '3':False, '3':False, '3':False ,'3':False}
    
    # first check if there is EVEN a possible solution
    # could check to see if it is 0, y# another check would be to see if it increases:
    if N == 0 or N == 2*N:
        return -1
    
    
    NTmp = copy.deepcopy(N)
    counter = 1
    
    while not all(found):
        NTmp = N*counter
        modval = 10
        while NTmp*10 >= modval:
            nextint = (NTmp%modval)/(modval/10)
            found[nextint] = True
            modval*=10
        counter+=1
        #print found
    return NTmp
        
infile = open(sys.argv[1],'r')

numcases = int(infile.readline().strip())
outfile = open(sys.argv[1].replace('.in','.out'),'w')
for n in range(numcases):
    N = int(infile.readline().strip())
    
    Nsleep = calculate(N)
    
    
    ans = str(Nsleep) if Nsleep != -1 else 'INSOMNIA'
    outfile.write("Case #" + str(n+1)+": " + ans + '\n')
    print ans

outfile.close()
