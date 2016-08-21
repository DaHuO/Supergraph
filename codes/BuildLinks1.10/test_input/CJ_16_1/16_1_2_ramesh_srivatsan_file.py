t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    l = {}
    for i in range(2*n-1):
        pp = str(raw_input()).split()
        for a in pp:
            if l.has_key(a):
                l[a]+=1
            else:
                l[a]=1
    li = []
    for key, value in l.iteritems():
        if value%2!=0:
            li.append(int(key))
    li.sort()
    li = [str(oo) for oo in li]
    print('Case #'+str(_+1)+': '+(' '.join(li)))