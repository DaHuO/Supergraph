def find_position(orig_length, depth, target):
    if depth == 1:
        return target
    return (orig_length ** (depth - 1)) * target + find_position(orig_length, depth - 1, (target + 1) % orig_length)

t = int(input())
for i in range(t):
    k, c, s = tuple(int(x) for x in input().split())
    if s * c < k:
        print("Case #%d: IMPOSSIBLE" % (i+1))
        continue
    l = []
    for j in range(0, k, c):
        l.append(find_position(k, c, j))
    print("Case #%d: %s" % (i+1, " ".join("%d" % (x+1) for x in l)))
    
