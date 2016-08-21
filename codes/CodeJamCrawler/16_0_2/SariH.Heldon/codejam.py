def pancake(s):
    c = 0
    flip = 0
    for x in s[::-1]:
        if x == '+' and flip == 0:
            pass
        elif x == '+' and flip == 1:
            c += 1
            flip ^= 1
        elif x == '-' and flip == 0:
            c += 1
            flip ^= 1
        elif x == '-' and flip == 1:
            pass
    return c

t = input()
for i in xrange(1, t+1):
    s = raw_input()
    print "Case #%d: %d" %  (i, pancake(s))
