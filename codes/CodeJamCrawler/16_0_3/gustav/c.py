N = 32
J = 500

def to_binstr(n):
    ret = ""
    while n:
        ret += str(n % 2)
        n /= 2
    return ret[::-1]

def interp_base(s, b):
    ret = 0
    for i in s:
        ret *= b
        if i == '1':
            ret += 1
    return ret

def maybe(s):
    divs = []
    for b in xrange(2, 11):
        witness = -1
        m = interp_base(s, b)
        for d in xrange(2, min(10000, m)):
            if m % d == 0:
                witness = d
                break
        if witness == -1:
            return []
        divs.append(witness)
    return divs

x = 2 ** (N - 1) + 1
print 'Case #1:'
for i in xrange(J):
    while not maybe(to_binstr(x)):
        x += 2
    print to_binstr(x), ' '.join([str(y) for y in maybe(to_binstr(x))])
    x += 2
