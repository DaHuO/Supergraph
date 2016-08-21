t = int(raw_input())

def ans(s):
        f = 0
        for i in xrange(1, len(s)):
                if s[i-1] != s[i]:
                        f = f+1
        if s[len(s)-1] == '-':
                f = f+1
        return f

for i in xrange(1, t+1):
        s = raw_input()
        print "Case #{}: {}".format(i, ans(s))
