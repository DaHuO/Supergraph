with open('A-large.in') as f:
    with open('a.out', 'w') as out:
        cases = f.readline()
        cases = int(cases)
        for i in xrange(1, cases+1):
            line = f.readline()
            res = line[0]
            for c in line[1:]:
                if c >= res[0]:
                    res = c+res
                else:
                    res = res+c
            y = ''.join(res[:-1])
            print 'Case #{i}: {y}'.format(y=y, i=i)
            out.write('Case #{i}: {y}\n'.format(y=y, i=i))