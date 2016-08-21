t =  int(raw_input())
for j in range(t):
    s = raw_input()
    ns = s[0]
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
            ns += s[i]
    if ns[-1] == '-':
        ans = len(ns)
    else:
        ans = len(ns)-1
    print "Case #" + str(j+1) + ': '+ str(ans)
