t = int(raw_input())

def find_all(s, dic, n):
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1

    if len(dic) == 10:
            return s

    return find_all(str(int(s) * n / (n - 1)), dic, n + 1)

for i in xrange(1, t + 1):
    m = raw_input().split(" ")

    if m[0] == '0':
        m[0] = 'INSOMNIA'
    else:
        m[0] = find_all(m[0], {}, 2)
    print "Case #{}: {}".format(i, m[0])
