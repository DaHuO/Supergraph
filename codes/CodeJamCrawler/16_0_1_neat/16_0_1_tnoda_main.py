def solve():
    x = y = input()
    s = set(str(x))
    i = 1
    while len(s) < 10:
        if i > 10000:
            return 'INSOMNIA'
        i += 1
        y += x
        s |= set(str(y))
    return y

T = input()
for i in range(1, T+1):
    ans = solve()
    print('Case #%d: %s' % (i, ans))
 

    
