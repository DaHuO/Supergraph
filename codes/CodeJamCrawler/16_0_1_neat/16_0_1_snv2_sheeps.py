__author__ = 'snv'
f = open('A-large.in','r')
n = int(f.readline())
for j in range(n):
    a = int(f.readline())
    ans = 'INSOMNIA'
    if a > 0:
        seen = set()
        for i in range (1,1000000):
            cur = a*i
            seen.update(set(k for k in str(cur)))
            if len(seen) == 10:
                ans = cur
                break
        else:
            print('wrong!!!!!!!!!!')
    print('Case #{0}: {1}'.format(j+1, ans))



