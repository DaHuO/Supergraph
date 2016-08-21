T = int(raw_input())

for t in range(T):
    S = raw_input()
    
    flip = 0
    for i in range(len(S) - 1):
        if S[i+1] != S[i]:
            flip += 1

    if S[-1] == '-':
        flip += 1

    res = flip
    print 'Case #%d: %s' % (t+1, res)