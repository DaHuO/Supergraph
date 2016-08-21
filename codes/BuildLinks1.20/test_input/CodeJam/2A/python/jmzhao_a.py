# -*- coding: utf-8 -*-
"""
@author: jmzhao
GCJ 2016 Round 2
"""

import sys
import collections

class IO :
    def get(reader=str) :
        return reader(input().strip())
    def gets(reader=str, delim=None) :
        return [reader(x) for x in input().strip().split(delim)]
    def tostr(raw, writer=str, delim=' ') :
        return delim.join(writer(x) for x in raw)

def prework(argv):
    '''do something according to argv,
    return a message describing what have been done.'''
    pass

nextd = {'P':'PR', 'R':'RS', 'S':'PS'}

def gennext(s) :
    if len(s) == 1 :
        return nextd[s]
    l = len(s) // 2
#    print(l)
    s1 = gennext(s[:l])
    s2 = gennext(s[l:])
    return s1 + s2 if s1 < s2 else s2 + s1

def once():
    '''to cope once'''
    n, r, p, s = IO.gets(int)
#    printerr((r, p, s), type(s))
    
    for init in ('P','R','S') :
        ss = init
        for _ in range(n) :
            ss = gennext(ss)
        printerr(repr(ss))
        c = dict.fromkeys('PRS',0)
        for x in ss :
            c[x] = c[x] + 1
#        printerr((c['R'], c['P'], c['S']), type(c['S']))
#        printerr(int(c['R']) == r, int(c['P']) == p, (c['S']) - s == 0)
#        printerr((c['R'], c['P'], c['S']) == (r, p, s))
        if all((int(c['R']) == r, int(c['P']) == p, (c['S']) == s)) :
            return ss
    return 'IMPOSSIBLE'

def show(ans) :
    return ans #IO.tostr(ans, writer=str, delim=' ')
    
def printerr(*v):
    print(*v, file=sys.stderr)

def main():
    TT = int(input())
    for tt in range(1,TT+1):
        printerr("coping Case %d.."%(tt))
        ans = once()
        print("Case #%d: %s"%(tt, show(ans)))

if __name__ == '__main__' :
    msg = prework(sys.argv)
    print("prework done with", msg, file=sys.stderr)
    main()
