from __future__ import division

f = open('input.txt')
f2 = open('output.txt', 'a')

T = int(f.readline())

for t in xrange(1, T+1):
    S = list(str(f.readline()))
    if S[-1] == '\n':
        S = S[:-1]
    print '\n'
    ans = 0
    for i in xrange(len(S) - 1, -1, -1):
        print S
        if S[i] == '-':
            ans += 1
            for j in xrange(i+1):
                if S[j] == '+':
                    S[j] = '-'
                else:
                    S[j] = '+'
    s = 'Case #' + str(t) + ': ' + str(ans) + '\n'
    f2.write(s)

f.close()
f2.close()