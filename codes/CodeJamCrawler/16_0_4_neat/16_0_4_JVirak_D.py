# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io
import math

def truth(guess,k):
    n=len(guess)
    tg=0
    for i in range(0,n):
        tg=tg*k
        tg=tg+guess[i]
        if (i<n-1):
            tg=tg-1
    return(tg)

def solveD(Li):
    K=Li[0]
    C=Li[1]
    S=Li[2]
    N=1+int(math.floor((K-0.01)/C))
    if N>S:
        return("IMPOSSIBLE")
    else:
        ret=[0] * N
        count=0
        for i in range(0,N):
            guess =[0] * C
            for j in range(0,C):
                count=count+1
                L=count
                if L>K:
                    L=1
                guess[j]=L
            trueguess=truth(guess,K)
            ret[i]=trueguess
    return(' '.join(map(str,ret)))
    
        
def solve(infname, outfname):
    L = codejam_io.read_simple(infname, int)
    results = [solveD(Li) for Li in L]
    codejam_io.write_simple(outfname,results)
    
    
#solve("Dsample.in", "Dsample.out")  
solve("D-large.in", "D-large.out")    
