def solve(n):
    ori = n
    dic = {}
    cnt = 0
    while len(dic) < 10:
        n = ori * (cnt + 1)
        s = str(n)
        # print(n)
        for x in s:
            # print(x)
            dic[x] = True
        cnt += 1

    return n

out = open('out.txt', 'w')
with open('A-large.in') as f:
    ca = 0
    for line in f:
        if ca == 0:
            ca += 1
            continue
        n = int(line.strip())
        # print(n)
        if n == 0:
            out.write('Case #{}: INSOMNIA\n'.format(ca))
            print('Case #{}: INSOMNIA'.format(ca))
        else:
            res = solve(n)
            out.write('Case #{}: {}\n'.format(ca, res))
            print('Case #{}: {}'.format(ca, res))
        ca += 1
        # if ca == 3:break
