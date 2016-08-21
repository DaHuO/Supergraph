#!/usr/bin/env python
# -*- coding: utf-8 -*-

e = [(0, 'ZERO'), (8, 'GEIHT'), (2, 'WTO'), (6, 'XSI'), (4, 'UFOR'), (5, 'FIVE'), (3, 'RTHEE'), (7, 'SEVEN'), (1, 'ONE'), (9, 'NINE')]

def solve(s):
    l = ''
    for i, d in e:
        st = s
        f = True
        while f:
            for c in d:
                if c in st:
                    st = st.replace(c, '', 1)
                else:
                    f = False
                    break
            if f == True:
                s = st
                l += str(i)
                #print l, s
    return ''.join(sorted(l))
    

if __name__ == "__main__":
	for case in xrange(1, 1+input()):
		print "Case #{0}: {1}".format(case, solve(raw_input())) # one string