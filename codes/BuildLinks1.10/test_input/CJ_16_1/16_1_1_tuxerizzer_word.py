#!/usr/bin/env python
"""
usage: python file.py < X-small/large.in
"""

def solve(s):
    low_i = 1000
    high_i = 1000
    arr = ['' for _ in range(2002)]
    arr[low_i] = s[0]
    for c in s[1:]:
        if c >= arr[low_i]:
            arr[low_i - 1] = c
            low_i -= 1
        else:
            arr[high_i + 1] = c
            high_i += 1
    return ''.join([i for i in arr if i])

def main():
    t = int(raw_input())
    for casenum in range(t):
        s = raw_input()
        res = solve(s)
        print 'Case #%d: %s' % (casenum + 1, res)

if __name__ == '__main__':
    main()
