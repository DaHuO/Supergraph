import fileinput

def solve(n):
    seen=[False]*10
    i=0
    tmp=n
    while(sum(seen)<10):
        i+=1
        tmp=n*i
        while tmp:
            seen[tmp%10]=True
            tmp/=10
        if i>1000000:
            return "INSOMNIA"
    return n*i

case=1


for line in fileinput.input():
    if not fileinput.isfirstline():
        print("Case #"+str(case)+": "+str(solve(int(line))))
        case+=1
