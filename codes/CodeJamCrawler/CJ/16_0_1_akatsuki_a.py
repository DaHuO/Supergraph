def slept(dp):
    #print dp
    for i in dp:
        if i == 0:
            return False
    return True


def magic():
    t = int(raw_input())
    for tc in xrange(t):
        res = 1
        n = int(raw_input())
        if n != 0:
            dp = [0]*10
            nstr = str(n)
            for j in nstr:
                dp[int(j)] = 1
            while not slept(dp):
                res += 1
                nstr = str(n*res)
                #print nstr
                for j in nstr:
                    dp[int(j)] = 1
            print "Case #%d: %s" % (tc+1, nstr)
        else:
            print "Case #%d: %s" % (tc+1, "INSOMNIA")
magic()