
L = 26

DIG = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
       "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
E = [None] * 10
for i, digit in enumerate(DIG):
    alpha = [0] * L
    for ch in digit:
        alpha[ord(ch) - ord('A')] += 1
    E[i] = tuple(alpha)


memo = {}


def find(last_nr, counter, phone_nr):
    if sum(counter) == 0:
        return phone_nr

    C = tuple(counter)
    if (last_nr, C) in memo:
        return memo[(last_nr, C)]

    ans = None
    for n in xrange(last_nr, 10):
        tmp = counter[:]
        flag = True
        for i in xrange(L):
            tmp[i] -= E[n][i]
            if tmp[i] < 0:
                flag = False
                break
        if flag:
            res = find(n, tmp, phone_nr + [n])
            if res is not None:
                ans = res
                break
    memo[(last_nr, C)] = ans
    return ans


def solve(t):
    memo.clear()

    S = raw_input()
    counter = [0] * L
    for ch in S:
        counter[ord(ch) - ord('A')] += 1

    phone_nr = find(0, counter, [])

    test = [0] * L
    for n in phone_nr:
        for i in xrange(L):
            test[i] += E[n][i]
    assert test == counter

    phone_nr = ''.join(map(str, phone_nr))
    print 'Case #%d: %s' % (t, phone_nr)


T = input()
for i in xrange(T):
    solve(i+1)
