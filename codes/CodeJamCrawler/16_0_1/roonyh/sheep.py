lines = [int(line) for line in open('A-large.in')]

for i in range(lines[0]):
    val = lines[i+1]

    if val == 0:
        print 'Case #%d: INSOMNIA' % (i+1)
        continue;

    j = 1
    s = set()
    while True:
        s.update(set(str(val*j)))
        if len(s) == 10:
            break;
        j = j+1

    print 'Case #%d: %d' % (i+1, val*j)
