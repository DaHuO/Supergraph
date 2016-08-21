fi = open('in.txt')
fo = open('out.txt', 'w')
cases = int(fi.readline())

for case in range(cases):
    n = int(fi.readline())

    if n == 0:
        fo.write('Case #' + str(case + 1) + ': INSOMNIA\n')
        continue
        
    a = []
    m = n
    while m > 0:
        a.insert(0, m % 10)
        m = m / 10

    a = [0, 0] + a
    m = len(a)
    r = set(range(10))

    s = [0 for _ in range(m)]
    b = False
    for k in range(1, 100 * n):
        for i in range(m - 1, -1, -1):
            s[i] += a[i]
            if s[i] > 9:
                s[i] %= 10
                s[i - 1] += 1

            if s[i] != 0 or i - 1 >= 0 and s[i - 1] > 0:
                r.discard(s[i])
            if len(r) == 0:
                b = True
                break

        if b:
            break

    fo.write('Case #' + str(case + 1) + ': ' + str(k * n) + '\n')

fi.close()
fo.close()
