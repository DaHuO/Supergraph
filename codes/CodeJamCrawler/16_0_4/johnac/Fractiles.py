


def solve(k,c,s):
    if k ==1:
        if s==1:
            return "1"
        else:
            return "IMPOSSIBLE"
    if c == 1:
        if s<k:
            return "IMPOSSIBLE"
        else:
            return " ".join(map(str,range(1,k+1)))
    if s<k-1:
        return "IMPOSSIBLE"
    else:
        return " ".join(map(str,range(2,k+1)))




fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    k,c,s=map(int,fin.readline().strip().split())
    fout.write("Case #"+str(case)+": "+str(solve(k,c,s))+"\n")