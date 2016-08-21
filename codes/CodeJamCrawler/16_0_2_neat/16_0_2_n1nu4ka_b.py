T = int(raw_input())

for t in range(1, T+1):
    s = raw_input()
    newS = ""
    for ch in s:
        if(len(newS) > 0 and newS[-1] == ch):
            continue
        newS += ch
    
    n = len(newS)
    if(newS[-1] == '+'):
        n -= 1
    print 'Case #%d: %d' % (t, n)
