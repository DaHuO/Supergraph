



def solve(stack):
    last,count = '',0
    for cake in stack:
        if cake != last:
            count+=1
        last = cake
    if stack[0] == "-" and count %2!=0:
        return count
    elif stack[0] == "+" and count %2==0:
        return count
    else:
        return count-1



fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    stack=list(str(fin.readline().strip()))
    fout.write("Case #"+str(case)+": "+str(solve(stack))+"\n")