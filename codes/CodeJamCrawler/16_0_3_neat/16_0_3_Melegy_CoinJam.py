def tobase(num,base):
    num=str(num)
    l =len(num)-1
    r=0
    for ch in num:
        if ch == '1':
            r+=base**l
        l-=1
    return r
def isprime(n):
    for j in xrange(2,int(n**0.5)+1):
        if n % j ==0 :
            return False,j
    return True,-1
def isnotprimeforall(n):
    r=[]
    for j in range(2,11):
        num=tobase(int(bin(n)[2::]),j)
        f,di=isprime(num)
        if f:
            return False,[]
        r.append(di)
    return True,r



def solve(ln,c):
    r=[]
    for i in range(1,65536,2):
        flag = True
        org=bin(i)[2::]
        if len(org) == ln and org[0] == "1" and org[-1]=="1":
            f,di=isnotprimeforall(i)
            if f:
                fout.write(org+" "+" ".join(map(str,di))+"\n")
                c-=1
                if c==0:
                    break


fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    n,j=map(int,fin.readline().strip().split())
    fout.write("Case #"+str(case)+":\n")
    solve(n,j)