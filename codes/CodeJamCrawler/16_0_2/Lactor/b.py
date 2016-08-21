T = input()
for k in range(T):
    s = raw_input()

    tot = 0
    first = True
    for i in range(0, len(s)-1):
        if s[i] == '-' and s[i+1] == '+':
            tot+= 2 - first
            first = False
        if s[i] == '+':
            first = False
    if s[len(s)-1] == '-':
        tot+= 2-first
            
    print "Case #%d: %d"%(k+1, tot)
    
