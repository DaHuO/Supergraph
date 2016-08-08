def main_code(x):
    N, R, P, S = tuple(map(int, input().split()))
    names = {'r' : 'R', 'p' : 'P', 's' : 'S'}
    for _ in range(N):
        p = P + R - S
        r = R + S - P
        s = S + P - R
        if p % 2 == 1 or p < 0 or s % 2 == 1 or s < 0 or r % 2 == 1 or r < 0:
            print("Case #" + str(x + 1) + ":", "IMPOSSIBLE")
            return
        P = p/2
        R = r/2
        S = s/2
        pp = "".join(sorted([names['r'], names['p']]))
        rr = "".join(sorted([names['r'], names['s']]))
        ss = "".join(sorted([names['s'], names['p']]))
        names = {'r' : rr, 'p' : pp, 's' : ss}
        
    assert P or R or S
    if P:
        print("Case #" + str(x + 1) + ":", names['p'])
    elif R:
        print("Case #" + str(x + 1) + ":", names['r'])
    elif S:
        print("Case #" + str(x + 1) + ":", names['s'])
    else:
        assert False

T = int(input())
for x in range(T):
    main_code(x)
