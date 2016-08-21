input_file = open('B-large.in', 'r')
out_file = open('B-res-large.out', 'w')

test_cases = int(input_file.readline())

d = {}

import copy

#full recursy
def f(x):
    if d.get(x) is not None:
        return d[x]

    d[x] = -1
    end = len(x) - 1
    while end >= 0 and x[end] == '+':
        end -= 1

    if end == -1:
        d[x] = 0
        return 0

    ll = list(x)
    res = -1
    for i in range(1, end + 2):
        ll2 = list(reversed(ll[:i]))
        for j in range(len(ll2)):
            if ll2[j] == '+':
                ll2[j] = '-'
            else:
                ll2[j] = '+'
        ll2.extend(ll[i:end + 1])
        # print(ll2)


        cur = f(''.join(ll2))
        if cur == -1:
            continue
        if res == -1 or cur + 1 < res:
            res = 1 + cur

    d[x] = res
    return res

dp = {}
dm = {}

def fp(x):
    if dp.get(x) is not None:
        return dp[x]

    dp[x] = -1
    end = len(x) - 1
    while end >= 0 and x[end] == '+':
        end -= 1

    if end == -1:
        dp[x] = 0
        return 0

    rm = end
    while rm >= 0 and x[rm] == '-':
        rm -= 1

    if rm == -1:
        dp[x] = 1
        return 1

    lm = 0
    while x[lm] == '-':
        lm += 1

    ll = list(x)

    res = fm(''.join(list(x[:rm + 1]))) + 1

    if lm > 0:
        ll2 = list(reversed(ll[:end+1]))
        for j in range(len(ll2)):
            if ll2[j] == '+':
                ll2[j] = '-'
            else:
                ll2[j] = '+'

        kkk = len(ll2) - 1
        while kkk >= 0 and ll2[kkk] == '+':
            kkk -= 1

        cur = fp(''.join(ll2[:kkk + 1]))

        if cur == -1:
            print('OOOOOOOOOUUGHH')
        res = min(res, 1 + cur)

    dp[x] = res
    return res

def fm(x):
    if dm.get(x) is not None:
        return dm[x]

    dm[x] = -1
    end = len(x) - 1
    while end >= 0 and x[end] == '-':
        end -= 1

    if end == -1:
        dm[x] = 0
        return 0

    rp = end
    while rp >= 0 and x[rp] == '+':
        rp -= 1

    if rp == -1:
        dm[x] = 1
        return 1

    lp = 0
    while x[lp] == '+':
        lp += 1

    ll = list(x)

    res = fp(''.join(list(x[:rp + 1]))) + 1

    if lp > 0:
        ll2 = list(reversed(ll[:end+1]))
        for j in range(len(ll2)):
            if ll2[j] == '+':
                ll2[j] = '-'
            else:
                ll2[j] = '+'

        kkk = len(ll2) - 1
        while kkk >= 0 and ll2[kkk] == '+':
            kkk -= 1

        cur = fm(''.join(ll2[:kkk + 1]))

        if cur == -1:
            print('OOOOOOOOOUUGHH')
        res = min(res, 1 + cur)

    dm[x] = res
    return res

# for i in range(1, 11):
#     d['+' * i] = 0
#     d['-' * i] = 1

# print(f('-----'))
#
# print(f('+--'))


for t in range(1, test_cases + 1):
    s = input_file.readline().strip()
    # res = f(s)

    # for x in d:
    #     if d[x] == -1:
    #         print(t, x)
    # if (t == 75):
    #     print(s, res)

    res2 = fp(s)
    # print(res, res2)
    out_file.write('Case #{:d}: {:d}\n'.format(t, res2))
# print(d['+--'])

