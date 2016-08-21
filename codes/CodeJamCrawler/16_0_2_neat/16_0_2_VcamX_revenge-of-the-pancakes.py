
def parse(s):
    s = s[0] + s
    pre = None
    ss = []
    for x in s:
        if pre != x:
            pre = x
            ss.append(x)
    return ss

n = input()
for i in range(1, int(n)+1):
    s = input()
    ss = parse(s)
    print('Case #{}: {}'.format(i, len(ss) - (0 if ss[-1] == '-' else 1)))

