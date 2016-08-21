def revenge_of_the_pancakes():
    S = raw_input().strip()
    cnt, prev_is_positive = 0, True
    for i in reversed(xrange(len(S))):
        if prev_is_positive and S[i] == '-':
           cnt += 1
        elif not prev_is_positive and S[i] == '+':
           cnt += 1
        prev_is_positive = (S[i] == '+')
    return cnt

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, revenge_of_the_pancakes())
