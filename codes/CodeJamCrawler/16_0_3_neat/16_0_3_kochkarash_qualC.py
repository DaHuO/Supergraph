import math
import sys
fileinput = sys.stdin

#import StringIO
#fileinput = StringIO.StringIO(inputstr)

def isJam(j):
    dl=[]
    for b in range(2,11):
        bases = [b**i for i in range(len(j))[::-1]]
        jrep = sum([x*y for x,y in zip (j,bases)])
        div = isPrime(jrep)
        if div is None:
            return None
        dl.append(div)
    return dl

def isPrime(n):    
    div=None;
    for d in range(2, int(math.sqrt(n))+1):
        if (n %d)==0:
            div=d
            break
    return div

def nextJ(j):
    js=j[1:len(j)-1]
    for i in range(len(js))[::-1]:
        if js[i]==0:
            js[i]=1
            break
        js[i]=0
    j[1:len(j)-1]=js
    return j 

def main(): 
    
    T=int(fileinput.readline().strip())
    for t in range(T):
        print "Case #%s: " % (t+1,)
        N,J=fileinput.readline().strip().split()
        N,J = int(N), int(J)
        sys.stdout.flush()
        c=0;
        j=[1]+[0]*(N-2)+[1]
        while (c<J):
            dl = isJam(j)
            if dl is not None:
                c +=1
                print "%s %s" % ("".join([str(ji) for ji in j]), " ".join([str(dli) for dli in dl]) )
                sys.stdout.flush()
            j=nextJ(j)
            
if __name__ == "__main__": main()            