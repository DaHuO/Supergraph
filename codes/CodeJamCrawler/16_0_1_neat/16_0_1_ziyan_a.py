import os
import sys

def count(x, digits):
    while x > 0:
        digits[x % 10] = True
        x /= 10

def solve(N):
    n = N
    digits = [False] * 10
    if n == 0:
        return None
    count(n, digits)
    while not all(digits):
        n += N
        if n > 1e11:
            return None
        count(n, digits)
    return n

def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        N = long(sys.stdin.readline().strip())
        result = solve(N)
        if result is None:
            print 'Case #%d: INSOMNIA' % (t + 1)
        else:
            print 'Case #%d: %d' % (t + 1, result)

if __name__ == '__main__':
    main()

