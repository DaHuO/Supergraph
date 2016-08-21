def last_word(s):
    word = s[0]
    front = word
    for c in s[1:]:
        if ord(c) < ord(front):
            word += c
        else:
            word = c + word
            front = c
    return word


T = int(raw_input())
for i in xrange(1, T+1):
    s = raw_input()
    print 'Case #{}: '.format(i), last_word(s)