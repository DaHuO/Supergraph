def build(word):
    ans = word[0]
    for c in word[1:]:
        if c >= ans[0]:
            ans = c + ans
        else:
            ans = ans + c
    return ans

for i in xrange(input()):
    word = raw_input().strip()
    print "Case #%d: %s" % (1 + i, build(word))
