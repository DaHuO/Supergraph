def checkFront(s,sp,ep):
    count = 0
    for i in range(sp,ep+1):
        if s[i]=='+':
            break
        else:
            count+=1
    return count
def checkRear(s,sp,ep):
    count = 0
    for i in range(ep,sp,-1):
        if s[i]=='+':
            break
        else:
            count+=1
    return count
def invert(s,ep,sp):
    for i in range(sp,ep+1):
        if(s[i]=='-'):
            s[i] = '+'
        else:
            s[i] = '-'
    return s
def solve(s,ep,sp):
    count = 0
    while(sp<=ep):
        a = checkFront(s,sp,ep)
        b = checkRear(s,sp,ep)
        if(a>=b and a>0):
            sp+=a;
            count+=1
        elif(b>a and b>0):
            ep-=b
            s = invert(s,ep,sp)
            count+=1
        if(sp==ep and s[sp]=='+'):
            break
    return count
t = int(raw_input())
lst = []
for _ in range(t):
    s = list(raw_input())
    sp = 0
    ep = len(s)-1
    for i in range(len(s)-1,0,-1):
        if(s[i]=='-'):
            break
        else:
            ep -= 1
    lst.append(solve(s,ep,sp))
for i in range(t):
    print "Case #%d: %d"%(i+1,lst[i])
