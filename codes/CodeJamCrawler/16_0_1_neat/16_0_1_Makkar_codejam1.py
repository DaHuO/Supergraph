from __future__ import division

f = open('input.txt')
f2 = open('output.txt', 'a')

T = int(f.readline())

for t in xrange(1, T+1):
    N = int(f.readline())
    ans = ''
    if N == 0:
        ans = 'INSOMNIA'
    else:
        digits = [False] * 10
        for i in xrange(1, 10000000):
            num = N * i
            while num > 0:
                d = num % 10
                num = num // 10
                digits[d] = True
            if False not in digits:
                ans = str(N * i)
                break
    print ans
    s = 'Case #' + str(t) + ': ' + ans + '\n'
    f2.write(s)

f.close()
f2.close()