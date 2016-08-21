def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


f = open('A-large.in')

count = num(f.readline())

# print count

for i in range(1, count + 1):
    n = num(f.readline())
    if n == 0:
        print 'Case #{}: INSOMNIA'.format(i)
    else:
        used = {}
        unused_count = 10
        t = n
        while unused_count > 0:
            # print n, t, unused_count
            str_t = str(t)
            for c in str_t:
                if c not in used:
                    used[c] = True
                    unused_count -= 1
            t += n
        print 'Case #{}: {}'.format(i, t - n)
