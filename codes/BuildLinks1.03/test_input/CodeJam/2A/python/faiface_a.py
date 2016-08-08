t = int(input())

for q in range(1, t+1):
    n, r, p, s = map(int, input().split())

    a, b, c = 'P', 'R', 'S'

    for _ in range(n):
        a, b, c = a + b, a + c, b + c

    print('Case #{}: '.format(q), end='')
    for o in (a, b, c):
        if o.count('R') == r and o.count('P') == p and o.count('S') == s:
            print(o)
            break
    else:
        print("IMPOSSIBLE")
