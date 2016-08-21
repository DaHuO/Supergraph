#!/usr/bin/env python
"""
usage: python file.py < X-small/large.in
"""

def remove(l, strng):
    for i in strng:
        l.remove(i)
    return l

def solve(s):
    l = list(s)
    r = []
    while 'Z' in l:
        remove(l, 'ZERO')
        r.append('0')

    while 'W' in l:
        remove(l, 'TWO')
        r.append('2')

    while 'X' in l:
        remove(l, 'SIX')
        r.append('6')

    while 'G' in l:
        remove(l, 'EIGHT')
        r.append('8')

    while 'H' in l:
        remove(l, 'THREE')
        r.append('3')

    while 'R' in l:
        remove(l, 'FOUR')
        r.append('4')

    while 'F' in l:
        remove(l, 'FIVE')
        r.append('5')

    while 'V' in l:
        remove(l, 'SEVEN')
        r.append('7')

    while 'O' in l:
        remove(l, 'ONE')
        r.append('1')

    while 'N' in l:
        remove(l, 'NINE')
        r.append('9')

    assert not l

    return ''.join(sorted(r))

def main():
    t = int(raw_input())
    for casenum in range(t):
        s = raw_input()
        res = solve(s)
        print 'Case #%d: %s' % (casenum + 1, res)

if __name__ == '__main__':
    main()
