N = input()
for n in range(N):
    S = raw_input()
    
    s = S[0]
    S = S[1:]

    for c in S:
        if c>=s[0]:
            s = c+s
        else:
            s +=c
    
    print 'Case #%d: %s'%(n+1, s)
