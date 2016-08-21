N = input()
for n in range(N):
    s = raw_input().strip()

    while s.count('--'):
        s = s.replace('--', '-')
    while s.count('++'):
        s = s.replace('++', '+')

    a = len(s)-1 + 1*(s[-1]=='-')

    print 'Case #%d: %d'%(n+1, a)

