__author__ = 'sumant'


if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        k, c, s = map(int, str(raw_input()).split())
        print 'Case #%s: %s' % (i+1, ' '.join([str(_x) for _x in range(1, k+1)]))
