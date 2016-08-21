#!/usr/bin/python

def func(inp):
    def last_zero(inp_l):
        for i in xrange(len(inp_l)-1,-1,-1):
            if lis[i] == 0:
                return i
        return -1            

    lis = [0 if ch == '-' else 1 for ch in inp]
    del lis[last_zero(lis) + 1 :]
    count = 0
    while lis:
        count += 1
        if lis[0] == 0:
            lis = [1 - val for val in lis]
            lis.reverse()
            del lis[last_zero(lis) + 1 :]
        else:
            for i in xrange(len(lis)):
                if lis[i] == 0:
                    break
                else:
                    lis[i] = 0
    return count

t = int(raw_input())
for i in xrange(1, t + 1):
    print "Case #{}: {}".format(i, func(raw_input()))
