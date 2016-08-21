import sys

def solve(f):
    s = f.readline()
    last_c = ''
    ans = 0
    for c in list(s):
        if c == '-' and not last_c == '-':
            if last_c == '+':
                ans = ans + 1
            ans = ans + 1
        last_c = c
    print ans

if __name__ == "__main__":
   f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
   t = int(f.readline())
   for i in range(1, t + 1):
       print 'Case #%d:' % (i),
       solve(f)
