f = open('input.txt')
n = int(f.readline())

out = open('output.txt', 'w')

for i in range(n):
    res = set()
    k = 1
    stnum = int(f.readline().strip())
    num = stnum
    print i
    if stnum == 0:
        out.write('case #{0}: {1}\n'.format(str(i + 1),'INSOMNIA'))
    else:
        while len(res) < 10:
            for j in range(len(str(num))):
                if str(num)[j] not in res:
                    res.add(str(num)[j])
            k += 1
            num = stnum * k
        out.write('case #{0}: {1}\n'.format(str(i + 1),str(stnum * (k-1))))

