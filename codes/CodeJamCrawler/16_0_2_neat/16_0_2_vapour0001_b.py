def solve(s):
    if '-' not in s: return 0
    ret = 0
    r = len(s) - 1
    l = 0
    while r >= 0:
        l = 0
        # print(l, r, s, "########")
        while r >= 0 and s[r] == '+':
            r -= 1
        flag = 0

        while l <= r and s[l] == '+':
            flag = 1
            s[l] = '-'
            l += 1
        ret += flag

        s = s[0:r+1][::-1]
        r -= l + flag
        for i in range(r + 1):
            if s[i] == '+':
                s[i] = '-'
            else:
                s[i] = '+'
        # print(l, r, s)
        ret += 1
        if '-' not in s[0:r+1]:
            break
    return ret


out = open('out.txt', 'w')
ca = 0
with open('B-large.in') as f:
    for line in f:
        if ca == 0:
            ca += 1
            continue
        s = line.strip()
        res = solve(list(s))
        out.write('Case #{}: {}\n'.format(ca, res))
        print('Case #{}: {}'.format(ca, res))
        ca += 1
