def solve():
    S = raw_input()
    ans = 0
    while '-' in S:
        if S[0] == '+':
            index = S.index('-')
            S = '-' * index + S[index:]
        else:
            index = S.find('+')
            if index == -1:
                index = len(S)
            S = '+' * index + S[index:]
        ans += 1
        #print S
    return ans

T = input()
for t in xrange(T):
    print 'Case #%d:' % (t + 1,), solve()
