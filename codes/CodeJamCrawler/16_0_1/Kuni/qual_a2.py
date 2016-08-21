#coding: utf-8

def calc():
    n = int(raw_input())
    if n==0: return "INSOMNIA"
    val = -1
    flags = [False]*10
    for i in xrange(1, 1000):
        val = n*i
        while val > 0:
            flags[val%10] = True
            val = val/10
        if all(flags):
            break
    return n*i

T = int(raw_input())
for t in xrange(T):
    val = calc()
    print "Case #{}: {}".format(t+1, val)
