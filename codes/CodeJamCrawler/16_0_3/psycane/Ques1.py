from sys import stdin as ip
def factors(n):    
    l=[]
    for i in range(2, 1000):
        q,r = n/i, n%i     
        if r == 0:
            l.append(i) 
    return l

dic={}
def gen(pos,n,cur,j):
    if pos>n:
        return
    if len(dic)==j:
        return
    if len(cur)==n:
        if not ok(cur):
            return
    gen(pos+1,n,cur+'0',j)
    gen(pos+1,n,cur+'1',j)

def ok(s):
    s='1'+s+'1'
    dic[s]=[]
    for i in xrange(2,11):
        c=int(s,i)
        fac=factors(c)
        if fac==[]:
            del dic[s]
            return False
        else:
            dic[s].append(fac[0])
    else:
        return True

f=open('op2.txt',"w")
for _ in xrange(int(ip.readline())):
    n,j=map(int,ip.readline().split())
    gen(0,n-2,'',j)
    f.write("Case #%d:\n"%(_+1))
    for i in dic:
        f.write(str(i)+" ")
        for j in dic[i]:
            f.write(str(j)+" ")
        f.write("\n")
f.close()
