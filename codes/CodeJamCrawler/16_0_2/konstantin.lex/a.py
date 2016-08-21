def solve(s):
    cnt = 0
    prev = s[0]
    for i in s[1:]:
        if i != prev:
            cnt += 1
        prev = i
    if s[-1] == '-':
        cnt += 1
    return cnt

f = open('in.txt', 'r')
t = int(f.readline().strip())
for i in range(t):
    n = f.readline().strip()
    res = solve(n)
    print "Case #{}: {}".format(i + 1, res)
