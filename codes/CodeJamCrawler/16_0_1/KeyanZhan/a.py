f = open('a.out', 'w')

n = input()
for i in range(0, n):
    f.write('Case #' + str(i + 1) + ': ')
    m = input()
    if (m == 0):
        f.write('INSOMNIA\n')
    else:
        visit = []
        c = 0
        while (True):
            c += m
            temp = c
            while (temp > 0):
                k = temp % 10
                if not k in visit:
                    visit += [k]
                temp /= 10
            if len(visit) >= 10:
                break
        f.write(str(c) + '\n')
f.close()