import sys

def parse(f):
    n = int(f.readline())
    return n,


def solve(n):
    if not n:
        return 'INSOMNIA'

    seen = [False] * 10
    def upseen(x):
        while x:
            seen[x % 10] = True
            x /= 10

    k = 0
    while not all(seen):
        k += 1
        upseen(k * n)
    return k * n


def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        inp = parse(sys.stdin)
        print 'Case #%s: %s' % (i+1, solve(*inp))
    

if __name__ == '__main__':
    main()
