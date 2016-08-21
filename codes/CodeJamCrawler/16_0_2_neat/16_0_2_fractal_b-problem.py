
T = int(raw_input())

def neg(x):
    if x == '+':
        return '-'
    elif x == '-':
        return '+'
    else:
        raise Exception("x value is not expected")

def find_flips(s):
    if '-' not in s:
        return 0
    if len(s) == 1:
        return 1
    flips = 0
    while '-' in s:
        x = s[0]
        n = s.find(neg(x))
        if n == -1:
            return flips+1
        s = neg(x)*n + s[n:]
        flips += 1

    return flips

for a in range(1,T+1):
    s = raw_input()
    print "Case #%d: %d" % (a, find_flips(s))

