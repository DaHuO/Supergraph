


def solve(k,c,s):
    r=[]
    jump=k**(c-1)
    for i in range(1,k**c+1,jump):
        r.append(str(i))
    return " ".join(r)



fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    k,c,s=map(int,fin.readline().strip().split())
    fout.write("Case #"+str(case)+": "+str(solve(k,c,s))+"\n")