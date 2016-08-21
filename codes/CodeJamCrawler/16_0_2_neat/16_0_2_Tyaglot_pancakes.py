import fileinput
filename=""
case=1

def solve(r):
    r=list(r)
    r[-1]="+"
    last=r[0]
    count=0
    for c in r:
        if c!=last:
            last=c
            count+=1
    return count



for line in fileinput.input():
    if not fileinput.isfirstline():
        print("Case #"+str(case)+": "+str(solve(line)))
        case+=1

