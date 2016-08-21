# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io

def flipit(rope):
    n=len(rope)
    nrope=rope
    cut=0
    if (rope[0]==0):
        stop=0
        for i in range(0,n):
            if stop==0:
                if nrope[i]==0:
                   cut=i
                if nrope[i]==1:
                    stop=1
    if (rope[0]==1):
        for i in range(0,n):
                if nrope[i]==0:
                   cut=i
    B=nrope[0:cut+1] 
    for i in range(0,len(B)):
        B[i]=1-B[i]
    nrope[0:cut+1]=B         
    return(nrope)

def solveB(Li):
    rope=Li[0]
    nli=[0] * len(rope)
    k=len(rope)
    for i in range(0,k):
        if rope[i]=="+":
            nli[i]=1
    flips=0
    while (sum(nli)<len(nli)):
        nli=flipit(nli)
        flips=flips+1
    return(flips)
        
def solve(infname, outfname):
    L = codejam_io.read_simple(infname, str)
    for Li in L:
        print(Li)
    results = [solveB(Li) for Li in L]
    codejam_io.write_simple(outfname,results)
    
    
    
solve("B-large.in", "B-large.out")    
#solve("Bsample.in", "Bsample.out")
