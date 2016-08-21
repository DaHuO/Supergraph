import sys

f = open(sys.argv[1])
r = open(sys.argv[2], 'w')

tcnt = int(f.readline().strip())

for i in xrange(tcnt):
    pc = f.readline().strip()

    resultstr = 'Case #%d: ' % (i + 1)

    i = 0
    cost = 1

    total_cost = 0

    while i < len(pc):
        if pc[i] == '+':
            while i < len(pc) and pc[i] == '+':
                i += 1

            cost = 2
        else:
            total_cost += cost
            while i < len(pc) and pc[i] == '-':
                i += 1

    resultstr = '%s %d\n' % (resultstr, total_cost)
    print resultstr
    r.write(resultstr)
    

f.close()
r.close()
