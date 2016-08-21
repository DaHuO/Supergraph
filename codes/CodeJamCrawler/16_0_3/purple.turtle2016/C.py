from math import *
import itertools
def is_prime(n):
    if n<2:
        return 0
    if n%2==0:
        return 2

    limit = int(sqrt(n))
    i=3
    while i<limit:
        if n%i==0:
            return i
        i+=2
    return 0

def generate_jamcoin(n,j):
    count=0
    res=[]
    for k in itertools.product("01", repeat=n):

        if k[0]=='0' or k[-1]=='0':
            continue
        proof=[]
        s="".join(k)
        for b in range(2,11):

            n=int(s,b)
            i=is_prime(n)
            if i==0:
                break
            else:
                proof.append(i)
        if len(proof)==9:
            res.append((s,proof))
        if len(res)==j:
            break
    return res


file_name="C-small-attempt2"
f=open(file_name+".in","r")
t=int(f.readline().strip("\n"))
f2=open(file_name+".out","w")
for i in range(1,1+t):
    n,j=[int(k) for k in f.readline().strip("\n").split()]

    f2.write("Case #"+str(i)+": "+"\n")
    res=generate_jamcoin(n,j)
    for s,proof in res:
        f2.write(s)
        for i in proof:
            f2.write(" "+str(i))
        f2.write("\n")

f.close()
f2.close()