import sys

f = open(sys.argv[1])
r = open(sys.argv[2], 'w')

tcnt = int(f.readline().strip())

for i in xrange(tcnt):
    n = int(f.readline().strip())

    resultstr = 'Case #%d: ' % (i + 1)
    if n == 0:
        resultstr += 'INSOMNIA'
        print resultstr
        r.write(resultstr + '\n')
        continue

    ds = set(['0', '1', '2', '3', '4', '5', '6', '7', '8','9'])

    cnt = 0
    val = n
    while len(ds) > 0:
        val_str = str(val)
        for i in xrange(len(val_str)):
            if val_str[i] in ds:
                ds.remove(val_str[i])

        val += n
        cnt += 1

    resultstr += str(cnt * n)

    print resultstr
    r.write(resultstr + '\n')
    

f.close()
r.close()
