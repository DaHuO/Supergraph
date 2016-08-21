import sys

def do(T):
    nums = set()
    x = 1
    seen = set()
    while True:
        n = T * x
        if n in seen:
            break
        seen.add(n)

        for c in str(n):
            nums.add(c)

        if len(nums) == 10:
            return n

        x = x + 1

    return 'INSOMNIA'

N = int(sys.stdin.readline())
for i in range(N):
    T = int(sys.stdin.readline())
    r = do(T)
    print 'Case #%d: %s' % (i + 1, r)

