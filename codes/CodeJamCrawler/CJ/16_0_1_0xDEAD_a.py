import sys

limit = sys.maxsize/2

def solve(n):
    a = list(n)
    s = set(a)
    ans = int(n)
    tn = int(n)
    if int(n) == 0:
       return -1
    ctr = 1;
    while tn <= limit:
        ctr += 1
        tn = ans*ctr
        tl = list(str(tn))
        for i in tl:
            s.add(i)
        if len(s) == 10:
            break
    if tn > limit:
        return -1
    else:
        return tn

a = raw_input()
print a

for i in range(0,int(a)):
    t = raw_input()
    ans = solve(t)
    if ans == -1:
       print "Case #"+str(i+1)+": INSOMNIA"
    else:
       print "Case #"+str(i+1)+": "+str(ans)

   

