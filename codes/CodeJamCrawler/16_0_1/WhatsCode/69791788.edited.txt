T = int(raw_input())
for i in xrange(T):
    s = raw_input()
    ans = ''
    for c in s:
        if ans == '':
            ans += c
        elif c >= ans[0]:
            ans = c + ans
        else:
            ans = ans + c
    print "Case #"+str(i+1)+": " + ans