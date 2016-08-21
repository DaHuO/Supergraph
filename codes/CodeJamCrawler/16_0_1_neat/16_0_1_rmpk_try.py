def makelist(a, z):
    g = [int(x1) for x1 in str(a)]
    g.extend(z)
    h = list(set(g))
    return h


def mainfunc():
    x = file.readline()
    x = x.strip()
    if int(x) == 0:
        nextnum = 'INSOMNIA'
        return nextnum
    z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 2
    y = [int(x1) for x1 in str(x)]

    while y != z:
        nextnum = i * int(x)
        listcompare = makelist(nextnum, y)
        y = listcompare
        i += 1

    return nextnum


file = open('A-large.in.txt', 'r')
file1 = open("Output.txt", "w")
count = int(file.readline())
for i in range(count):
    number = mainfunc()
    file1.write('Case #{}: {}\n'.format(i + 1, number))
    print('Case #{}: {}'.format(i + 1, number))
file1.close()
file.close()
