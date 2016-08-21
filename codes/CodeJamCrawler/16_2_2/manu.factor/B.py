#!/bin/python
import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')
    
T = int(input.readline())

def minimum(pattern):
    return pattern.replace('?','0')

def maximum(pattern):
    return pattern.replace('?','9')

def distance(p,s):
    return (p, s, abs(int(p)-int(s)))

def closer(p,s):
    if not p:
        assert not s
        return ('','')
    lst = []
    if p[0] == '?' and s[0] == '?':
        pp, ss = closer(p[1:],s[1:])
        pp = '0' + pp
        ss = '0' + ss
        lst.append(distance(pp,ss))
        
        pp, ss = minimum(p[1:]), maximum(s[1:])
        pp = '1' + pp
        ss = '0' + ss
        lst.append(distance(pp,ss))

        pp, ss = maximum(p[1:]), minimum(s[1:])
        pp = '0' + pp
        ss = '1' + ss
        lst.append(distance(pp,ss))
    elif p[0] == '?':
        pp, ss = closer(p[1:], s[1:])
        pp = s[0] + pp
        ss = s[0] + ss
        lst.append(distance(pp,ss))

        if s[0] != '9':
            pp, ss = minimum(p[1:]), maximum(s[1:])
            pp = str(int(s[0])+1) + pp
            ss = s[0] + ss
            lst.append(distance(pp,ss))

        if s[0] != '0':
            pp, ss = maximum(p[1:]), minimum(s[1:])
            pp = str(int(s[0])-1) + pp
            ss = s[0] + ss
            lst.append(distance(pp,ss))
    elif s[0] == '?':
        pp, ss = closer(p[1:], s[1:])
        pp = p[0] + pp
        ss = p[0] + ss
        lst.append(distance(pp,ss))

        if p[0] != '9':
            pp, ss = maximum(p[1:]), minimum(s[1:])
            ss = str(int(p[0])+1) + ss
            pp = p[0] + pp
            lst.append(distance(pp,ss))

        if p[0] != '0':
            pp, ss = minimum(p[1:]), maximum(s[1:])
            ss = str(int(p[0])-1) + ss
            pp = p[0] + pp
            lst.append(distance(pp,ss))
    else:
        if p[0] == s[0]:
            pp, ss = closer(p[1:], s[1:])
        elif p[0] > s[0]:
            pp, ss = minimum(p[1:]), maximum(s[1:])
        else:
            assert p[0] < s[0]
            pp, ss = maximum(p[1:]), minimum(s[1:])
        pp = p[0] + pp
        ss = s[0] + ss
        return pp, ss

    lst.sort(key=lambda (p,s,d): (d,p,s))
    print p,s, lst
    return (lst[0][0], lst[0][1])
        
        
def solve():
    p, s = input.readline().strip().split(' ')
    p, s  = closer(p,s)
    return '{} {}'.format(p,s)
    
for t in range(T):
    print >> output, 'Case #%s: %s' % (t+1,solve())

