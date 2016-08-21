def f(s):
    ans = 0
    if len(s) > 2:
        for i in xrange(1,len(s)):
            if s[i-1] + s[i] == '+-':
                ans += 2
    else:
        if '+-' in s:
            ans += 2

    if s[0] == '-':
        ans += 1
    return ans


F = open('B-large.in')
A = F.read()
A = A.split('\n')[1:-1]
Ans = map(f,A)


E = open('Ans2.large','w')
for i in xrange(len(Ans)):
    E.write('Case #' + str(i+1) + ': ' + str(Ans[i]) + '\n')
E.close()   

