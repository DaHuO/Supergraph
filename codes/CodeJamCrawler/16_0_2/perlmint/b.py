import sys
f = sys.stdin
total = int(f.readline())
for count in range(1, total + 1):
    p = [c for c in f.readline().strip()]
    c = 0
    for i in range(0, len(p)):
        if all(map(lambda x: x == '+', p)):
            break
        prev = p[0]
        swap_p = len(p)
        for j in range(1, len(p)):
            if p[j] != prev:
                swap_p = j
                break
        if swap_p:
            p = map(lambda x: '-' if x == '+' else '+',
                    reversed(p[0:swap_p])) + p[swap_p:]
        c += 1
    print "Case #{0}: {1}".format(count, c)
