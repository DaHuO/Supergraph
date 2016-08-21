import sys

def parse(f):
    s = f.readline().rstrip()
    return s,


def solve(s):
    curr = '+'
    flips = 0
    for c in reversed(s):
        if c != curr:
            curr = c
            flips += 1
    return flips


def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        inp = parse(sys.stdin)
        print 'Case #%s: %s' % (i+1, solve(*inp))
    

if __name__ == '__main__':
    main()
