t = int(raw_input())
for c in xrange(1, t+1):
    s = list(raw_input())
    last_word = s[0]
    c_word = s[0]
    for i in xrange(1, len(s)):
        if (c_word > s[i]):
            last_word = last_word + s[i]
        else:
            last_word = s[i] + last_word
            c_word = s[i]
    print "Case #{}: {}".format(c, last_word)
        


