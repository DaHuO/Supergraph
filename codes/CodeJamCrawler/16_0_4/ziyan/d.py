import os
import sys

def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        K, C, S = map(int, sys.stdin.readline().strip().split())
        result = None
        if S >= K:
            result = list(range(K))
        if result is None:
            print 'Case #%d: IMPOSSIBLE' % (t + 1)
        else:
            print 'Case #%d: %s' % (t + 1, ' '.join([str(i + 1) for i in result]))

if __name__ == '__main__':
    main()

