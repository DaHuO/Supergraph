case = int(raw_input())
for c in xrange(1,case+1):
    ps = raw_input()
    
    h_up = None
    ans = 0
    for p in ps:
        if h_up == None:
            h_up = (p == '+')
        else:
            if (h_up and p == '-') or (not h_up and p == '+'):
                h_up = not h_up
                ans += 1

    if not h_up:
        ans += 1

    print "Case #%d: %s"%(c, ans)
