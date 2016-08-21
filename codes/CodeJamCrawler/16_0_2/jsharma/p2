#!/c/Python27/python

import sys

def calc(s):
    cnt = 0
    cc = None
    for c in s:
        if c !='\n' and cc != c:
            if cc is not None:
                cnt += 1
            cc = c
    if cc == '-':
        cnt += 1

    return cnt


def main():
    N = int(sys.stdin.readline())
    ns = []
    for i in range(N):
        s = sys.stdin.readline()
        print 'Case #%d: %s' % (i + 1, calc(s))

if __name__ == '__main__':
    main()
