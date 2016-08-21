'''
Created on Apr 8, 2016

@author: TigerZhao
'''

f=open("B-large.in","r")
fout=open("test2.out","w")
cases = int(f.readline().strip())

def getOpposite(x):
    if x =="+":
        return "-"
    return "+"

def solve(line):
    if line ==["+"]:
        return 0
    if line==["-"]:
        return 1
    moves=0 
    while True:
        if "-" not in line:
            return moves
        moves+=1
        first=line[0]
        for p in range(len(line)):
            if line[p] ==first:
                line[p]= getOpposite(line[p])
            else:
                break
        
            
            
    return moves
                
    
    
    

for i in xrange(cases):
    line= list(f.readline().strip())

    fout.write("Case #{0}: {1}\n".format(i+1, solve(line) ))



fout.close()
f.close()