t=int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    if n == 0:
        ans = "INSOMNIA"
    else:
        ans = 0
        c,flag = 1, True
        number = set()
        while flag:
            temp = str(n*c)
            for j in temp:
                number.add(int(j))
            if len(number) == 10:
                flag = False
                ans = temp
            c+=1
    print 'Case #{}: {}'.format(i+1, ans)