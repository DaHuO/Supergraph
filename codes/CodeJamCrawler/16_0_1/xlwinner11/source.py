fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

T = int(fin.readline())
for test in range(1, T + 1):
    n = int(fin.readline())
    if (n == 0):
        print("Case #", test, ": INSOMNIA", sep='', file=fout)
    else:
        i = 1
        k = set()
        while (len(k) != 10):
            tmp = str(n * i)
            for el in tmp:
                k.add(el)
            i += 1
        print("Case #", test, ": ", n * (i - 1), sep = '', file=fout)

fin.close()
fout.close()