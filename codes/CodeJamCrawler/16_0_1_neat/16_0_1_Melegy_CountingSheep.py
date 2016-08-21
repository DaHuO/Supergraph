
def solve(num):
    if num ==0:
        return "INSOMNIA"
    seen=set()
    i = 1
    while(len(seen))<10:
        last = num * i
        seen.update(list(str(last)))
        i+=1
    return last



fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    num=int(fin.readline().strip())
    fout.write("Case #"+str(case)+": "+str(solve(num))+"\n")