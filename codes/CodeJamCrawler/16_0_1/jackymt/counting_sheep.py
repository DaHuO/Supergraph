def update(n, d):
    for c in str(n):
        d[int(c)] = True

def solution(n):
    i = 1
    d = {}
    while True:
        x = i * n
        update(x, d)
        if len(d) == 10:
            return x
        elif (i-1) * n == x:
            return 'INSOMNIA'
        i += 1

with open('A-large.in.txt', 'r') as f:
    for i, line in enumerate(f):
        if i > 0:
            n = int(line)
            x = solution(int(n))
            print "Case #{}: {}".format(i, x)