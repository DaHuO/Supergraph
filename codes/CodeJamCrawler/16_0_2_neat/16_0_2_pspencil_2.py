t = int(raw_input())
for i in range(1,t+1):
    print "Case #"+str(i)+":",
    s = raw_input()
    ans = 0
    p = ''
    for i in s:
        if p == '':
            p = i
        else:
            if p!=i:
                ans += 1
            p=i
    if s[-1] == '-':
        ans += 1
    print ans
