#!/usr/bin/env python

def reduce(st):
    # remove duplicate +- things
    res = st[0]
    for c in st[1:]:
        if res[-1] != c:
            res += c
    return res

def revenge(st):
    """
    '-' costs 2 if in the middle, 1 otherwise
    """
    st = reduce(st)
    cost = 0
    
    if st[0] == '-':
        cost += 1
        st = st[1:]

    if len(st) == 0:
        return cost

    # print st
    st = st.split('+')

    if st[0] == '':
        st = st[1:]
    if st[-1] == '':
        st = st[:-1]

    return cost + len(st)*2
    

for idx in range(1, input()+1):
    print "Case #%d:"%idx, revenge(raw_input())
    
