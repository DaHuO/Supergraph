N = 32
J = 500
l = (N - 4) / 2

def dec2base(dec, base):
    s = []
    while dec != 0:
        s.append(dec % base)
        dec = dec / base
    return ''.join([str(i) for i in s[::-1]])

def base2dec(string, base):
    s = 0
    t = 1
    for i in string[::-1]:
        s += t*int(i)
        t = t*base
    return s

print "Case #1:"
for i in xrange(J):
    t = dec2base(i+5, 2)
    t = (l-len(t)) * "0" + t
    print "1{}11{}1".format(t, t),
    for j in xrange(9):
        s = "1{}1".format(t)
        #print s
        print base2dec(s, j+2),
    print

