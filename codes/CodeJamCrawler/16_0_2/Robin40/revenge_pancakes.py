T = input()
for t in xrange(1, T+1):
    s = raw_input()

    ans = 0
    last = 'z'
    for c in s:
        if c != last:
            ans += 1
        last = c
    if last == '+':
        ans -= 1

    print "Case #" + str(t) + ": " + str(ans)
