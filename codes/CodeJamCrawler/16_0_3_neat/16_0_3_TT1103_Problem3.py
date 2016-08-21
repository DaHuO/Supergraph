'''
Created on Apr 8, 2016

@author: TigerZhao
'''
import itertools
f=open("C-small-attempt1.in","r")
fout=open("test3.out","w")
cases = int(f.readline().strip())

def isPrime(n):
    if n in [2,3,5,7,11]:
        return True,1
    if n%2==0:
        return False,2
    if n%3==0:
        return False,3
    i =5

    while i*i <n:
        if n%i == 0: 
            return False,i
        if n%(i+2) == 0: 
            return False,i+2
        i +=6
    return True,1


def solve(n,j):
    global fout
    r = itertools.product("10",repeat=n-2);           
    cnt =0 
    for comb in r:
        if cnt >=j:
            return
        c="".join(comb)
        line = "1"+c+"1"
        good =True
        evidence=""
        for x in xrange(2,11):
            prime,proof = isPrime(int(line,x))
            evidence +=str(proof)+" "
            if prime:
                good=False
                break
        if not good:
            continue

        fout.write(line+" "+evidence.strip()+"\n")
        cnt+=1
   
        
        
        
    
for i in xrange(cases):
    line= f.readline().strip().split()
    fout.write("Case #1:\n")
    N=int(line[0])
    J=int(line[1])

    solve(N,J)
    

fout.close()
f.close()