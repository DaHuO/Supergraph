

def f(n):
    left = set(range(10))
    m = n
    while left:
        k = m
        while k > 0:
            digit = k % 10
            if digit in left:
                left.remove(digit)
            k /= 10
            if not left:
                return m
        if k == m:
            return 'INSOMNIA'
        m += n
    return m


t = int(raw_input())
for i in range(t):
    print 'Case #%d:' % (i+1), f(int(raw_input()))
# cases = [0, 1, 2, 11, 1692]

# for n in cases:
    # print f(n)
