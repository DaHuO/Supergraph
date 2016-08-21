def work(s):
    l = []
    for t in s:
        if t == "+": l.insert(0,1)
        else: l.insert(0,0)
    c = 0
    while sum(l) != len(s):
        i = l.index(0)
        if l[-1] and not l[i]:
            x = len(l)-1
            while l[x]:
                l[x] = 0
                x-=1
        else:
            tmp = l[i:]
            l = l[:i] + [(x + 1) % 2 for x in tmp[::-1]]
        c+=1
    return c
        

a = open("B-large.in").readlines()
N = int(a.pop(0))
        
for i in range(N):
    r = work(a.pop(0).strip())
    print "Case #"+str(i+1)+":", r
