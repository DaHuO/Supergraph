from sys import stdin


T = int(stdin.readline())
for c in range(1,T+1):
    s = []
    s.extend(stdin.readline().strip())
    l = len(s)
    n = reduce(lambda x, y: 2*x + y,
               reversed([0 if x == '+' else 1 for x in s]))
    ops = 0
    if n != 0:
        for i in reversed(range(l)):
            if n == 0:
                break
            if n & (1<<i):
                n ^= (1<<(i+1))-1
                ops += 1
    
    print "Case #{}: {}".format(c, ops)
