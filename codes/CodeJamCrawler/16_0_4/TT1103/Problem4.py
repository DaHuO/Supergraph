'''
Created on Apr 8, 2016

@author: TigerZhao
'''
import itertools
f=open("D-small-attempt3.in","r")
fout=open("test4.out","w")
cases = int(f.readline().strip())


def solve(k,c,s):
    global fout
    if k==1:
        return 1
    positions = []
    for i in range(k):
        newPos = i*(k**(c-1)) +1
        positions.append(str(int(newPos)))
    return (" ".join(positions)).strip()

        
        
        
    
for i in xrange(cases):
    line = f.readline().strip().split()
    k=int(line[0])
    c=int(line[1])
    s=int(line[2])
    
    fout.write( "Case #{0}: {1}\n".format(i+1,solve(k,c,s)))

    
    
    

fout.close()
f.close()