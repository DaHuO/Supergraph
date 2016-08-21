for tc in xrange(input()):
    ans = "INSOMNIA"
    n = input()
    on = n
    if n != 0:
        s = set("1234567890")
        while len(s):
            ans = str(n)
            s -= set(ans)
            n += on
    print "Case #%d: %s" % (tc+1, ans)
