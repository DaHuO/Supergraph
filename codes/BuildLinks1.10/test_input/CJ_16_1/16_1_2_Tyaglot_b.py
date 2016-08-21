import fileinput
from operator import itemgetter


def solve(S):
    mixed,N=S
    ret=[]
    for i in mixed:
        for j in i:
            if j in ret:
                ret.remove(j)
            else:
                ret.append(j)
    ret=[int(i) for i in ret]
    return ' '.join([str(i) for i in sorted(ret)])
    
        
    

lines=iter(fileinput.input())

for line in lines:
    max_case=int(line)
    for case in range(max_case):
        N=int(next(lines))
        mixed=[]
        for i in range(2*N-1):
            mixed.append(next(lines).replace('\n','').split(' '))
        print "Case #"+str(case+1)+": "+solve((mixed,N))
