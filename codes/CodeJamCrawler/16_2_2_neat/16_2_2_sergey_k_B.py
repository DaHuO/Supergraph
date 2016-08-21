
import sys

options = (0,0), (0,1), (0,9), (9,0), (1,0)

def solve(a, b, i):
    if i == len(a):
        x, y = int(a), int(b)
        return (abs(x - y), x, y, a, b)

    if a[:i] != b[:i]:
        less = a[:i] < b[:i]
        a = a.replace('?', '9' if less else '0')
        b = b.replace('?', '0' if less else '9')
        x, y = int(a), int(b)
        return (abs(x - y), x, y, a, b)
    
    if a[i] == '?' and b[i] == '?':
        res = None
        for c1, c2 in options:
            aa = a.replace('?', str(c1), 1)
            bb = b.replace('?', str(c2), 1)
            t = solve(aa, bb, i + 1)
            if res is None or t < res: res = t
        return res
    if a[i] == '?':
        res = solve(a.replace('?', b[i], 1), b, i + 1)
        for d in (-1, 1):
            n = (int(b[i]) + d + 10) % 10
            t = solve(a.replace('?', str(n), 1), b, i + 1)
            if t < res: res = t
        return res
    if b[i] == '?':
        res = solve(a, b.replace('?', a[i], 1), i + 1)
        for d in (-1, 1):
            n = (int(a[i]) + d + 10) % 10
            t = solve(a, b.replace('?', str(n), 1), i + 1)
            if t < res: res = t
        return res
    return solve(a, b, i + 1)
    

def main():
    T = int(sys.stdin.readline())
    for i in xrange(T):
        a, b = sys.stdin.readline().strip().split(' ')
        _, _, _, x, y = solve(a, b, 0)
        print "Case #%d: %s %s" % (i + 1, x, y)

if __name__ == '__main__':
    main()
