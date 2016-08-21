t = int(raw_input())
for tt in xrange(t) :
    print "Case #" + str(tt+1) + ": ",
    n = raw_input()
    ans = 0
    while '-' in n :
        x = n.rfind('-')
        z = ""
        for i in range(x+1) :
            if n[i] == '+' :
                z += '-'
            else :
                z += '+'
        z = z + n[x+1:]
        n = z
        ans += 1
    print ans