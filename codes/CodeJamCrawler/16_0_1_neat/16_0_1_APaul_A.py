#!/usr/bin/local/python

def check(n):
    if n == 0:
        return "INSOMNIA"
    ds = {'0': 0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0 }
    add = n
    while(True):
        nstr = str(n)
        for c in nstr:
            ds[c] += 1
        # cnts = [ v for k,v in ds.iteritems() ]
        if [ v for k,v in ds.iteritems() ].__contains__(0):
            n += add
        else:
            return n

outs = [ check(int(raw_input())) for __ in xrange(int(raw_input())) ]

for itr,o in enumerate(outs):
    print "Case #{}: {}".format(itr+1, o)
