
def sheep(n, case):
    complete = set(range(10))
    incomplete = set()
    i = 1
    n = int(n)
    nxi = int()
    if n == 0:
        print 'Case #%s: INSOMNIA' % (case)
    else:
        while incomplete != complete:
            nxi = n * i
            incomplete.update([int(num) for num in str(nxi)])
            i += 1
        print 'Case #%s: %s' % (case, str(nxi))

filename = 'A-large.in'
for idx, row in enumerate(open(filename, 'r')):
    if idx == 0:
        T = row
    else:
        case = str(idx)
        sheep(row, case)
