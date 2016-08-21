# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io


def solveA(Li):
    n=Li[0]
    if (n==0):
        return("INSOMNIA")
    if (n>0):
        seen=[0] * 10
        count=1
        while (min(seen)<0.1):
            m=n*count
            while (m>0.5):
                b=m%10
                seen[b]=seen[b]+1
                m=(m-b)/10
            count=count+1    
        return(n*(count-1))
        
def solve(infname, outfname):
    L = codejam_io.read_simple(infname, int)
    results = [solveA(Li) for Li in L]
    codejam_io.write_simple(outfname,results)
    
    
    
solve("A-large.in", "A-large.out")    
#solve("Bsample.in", "Bsample.out")
