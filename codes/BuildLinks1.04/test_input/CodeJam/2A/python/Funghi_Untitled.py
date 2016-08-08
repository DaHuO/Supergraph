T = int(input())
for case in range(T):
    num = [1, 0, 0]
    n, r, p, s = map(int, input().split() )

    for i in range(n):
        num[0], num[1], num[2] = num[0]+num[2], num[1]+num[0], num[1]+num[2]

    if [p, r, s] == num:
        winner = 0
    elif [r, s, p] == num:
        winner = 1
    elif [s, p, r] == num:
        winner = 2
    else:
        print("Case #{}: IMPOSSIBLE".format(case+1))
        continue
    tree = [[] for i in range(n+1)]
    tree[0].append(winner)

    for i in range(1,n+1):
        for k in tree[i-1]:
            tree[i].append(k)
            tree[i].append((k+1) % 3)

    k = ["P", "R", "S"]
    res = ""
    for c in tree[n]:
        res += k[c]

    for i in range(1, n+1):
        length = 2**(i-1)
        for pos in range(0, 2**n, length*2):
            if res[pos:pos+length] > res[pos+length:pos+2*length]:
                res = res[:pos] + res[pos+length:pos+2*length] + res[pos:pos+length] + res[pos+2*length:]

    print("Case #{}: {}".format(case+1, res))