import fileinput

def solve(k,c,s):
    if k>c*s:
        return "IMPOSSIBLE"
    ret=[]
    total=0
    layer=0
    for i in range(k):
        total+=i*(k**(c-layer-1))
        layer+=1
        if (layer==c or i==k-1):
            layer=0
            ret.append(total+1)
            total=0
    return ' '.join([str(x) for x in ret])

case=1

for line in fileinput.input():
    if not fileinput.isfirstline():
        tmp=line.replace('\n','').split(' ')
        k=int(tmp[0])
        c=int(tmp[1])
        s=int(tmp[2])
        print("Case #"+str(case)+": "+solve(k,c,s))
        case+=1
