import math

print 'Case #1:'
J = 500

mx = 100000001
primeb = [1] * mx
primeb[0] = primeb[1] = 0
prime = []
for i in xrange(mx):
    if primeb[i]:
        for j in xrange(i * 2, mx, i):
            primeb[j] = 0
        prime.append(i)

f = (2 ** 31) + 1
stop = 2 ** 32

while J and f < stop:
    ans = []
    for i in xrange(2, 11):
        n = int(bin(f)[2:], i)
        k = 0
        mxp = min(math.sqrt(n), prime[-2])
        while prime[k] <= mxp:
            if (n % prime[k]) == 0:
                ans.append(prime[k])
                break
            k += 1
        if len(ans) < i - 1:
            break
    if len(ans) == 9:
        print '{} {}'.format(bin(f)[2:], ' '.join(map(str, ans)))
        J -= 1
    f += 2
