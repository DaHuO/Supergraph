ns = list()
for i in range(int(input())):
    ns.append(int(input()))

for t, n in enumerate(ns):
    if (n != 0):
        s = set()
        j = 1

        while (len(s) < 10):
            [s.add(k) for k in str(n * j)]
            j = j + 1

        print('Case #' + str(t + 1) + ': ' + str(n * (j - 1)))
    else:
        print('Case #' + str(t + 1) + ': INSOMNIA')
