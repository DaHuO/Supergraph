def getNumberSet(inp):
    ret = set()
    s = str(inp)
    for ch in s:
        ret.add(ch)
    return ret


test = int(raw_input())
for i in range(0,test):
    N = int(raw_input())
    nuSet = set()
    for j in range(1,101):
        nuSet = nuSet.union(getNumberSet(N*j))
        if len(nuSet) >= 10:
            print "Case #"+str(i+1)+": "+str(N*j)
            break
    if len(nuSet) < 10:
        print "Case #"+str(i+1)+": INSOMNIA"
