#!/usr/bin/env python

def last_word(st):
    res = st[0]
    st = st[1:]
    for ch in st:
        if ch + res >= res + ch:
            res = ch + res
        else:
            res = res + ch

    return res
        

for case in xrange(input()):
    print "Case #%d: %s"%(case+1, last_word(raw_input()))
