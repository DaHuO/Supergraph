import sys

def foo(ifile):
    n = int(ifile.readline())
    if n == 0:
        return 'INSOMNIA'
    res = [0] * 10
    a = n
    while True:
        n2 = n
        while n2 > 0:
            res[n2%10] = 1
            n2 //= 10
        if sum(res) == 10:
            return n
        n = n  + a



def main():
    ifile = sys.stdin
    n = int(ifile.readline())
    for i in range(n):
        print 'Case #%d: %s' % (i+1, foo(ifile))

main()

