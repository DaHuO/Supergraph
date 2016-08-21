file = open('code.in')
rows = []
for row in file:
    row = row.strip()
    rows.append(row)


t = int(rows[0])


def remove(lis, number):
    ns = str(number)
    for q in range(0, len(ns)):
        if int(ns[q]) in lis:
            del lis[lis.index(int(ns[q]))]
    return lis

for i in range(0, t):
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    n = int(rows[i + 1])
    x = n
    c = 2
    if n == 0:
        print "Case #{0}: INSOMNIA".format(i+1)
    else:
        while l:
            l = remove(l, x)
            if l:
                x = c * n
                c += 1
        print "Case #{0}: {1}".format(i + 1, x)
