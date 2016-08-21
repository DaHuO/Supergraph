from sys import stdin

T = int(stdin.readline())
for t in range(1,T+1):
    [k, c, s] = [int(x) for x in stdin.readline().split()]
    min_len = k/c + (1 if k%c > 0 else 0)
    grad = []
    if s >= min_len:
        grad = [0 for i in range(min_len)]
        for i in range(min_len):
            q = min(c, k-c*i)
            grad[i] = 1+reduce(lambda x, y: k*x+y, range(i*c, i*c+q) + [0 for w in range(i*c+q,i*c+c)])
    print "Case #{}: {}".format(t, " ".join([str(w) for w in grad]) if s >= min_len else "IMPOSSIBLE")
