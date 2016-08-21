T = int(raw_input())
for t in range(T):
    n = raw_input()
    res = 0
    tmp = ""
    tmp += n[0]
    for i in range(1, len(n)):
        if n[i] != tmp[-1]:
            tmp += n[i]
    if tmp[-1] == '+':
        res = len(tmp) -1
    else:
        res = len(tmp)
    print "Case #"+str(t+1)+": "+str(res)
