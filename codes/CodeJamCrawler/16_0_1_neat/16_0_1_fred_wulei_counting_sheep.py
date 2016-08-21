def sheep(num):
    if num == 0:
        return 'INSOMNIA'
    cur = num
    d = set()
    while len(d) < 10:
        n = str(cur)
        for c in n:
            if c not in d:
                d.add(c)
        cur += num
    return str(cur-num)

def solve(file):
    f = open(file, 'r')
    count = f.readline()
    case = 1
    for l in f.readlines():
        num = int(l.strip())
        print 'Case #%d: %s' % (case, sheep(num))
        case += 1



solve('A-large.in')
