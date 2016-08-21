from sys import stdin

T = int(stdin.readline())

for case in xrange(1,T+1):
    s = list(stdin.readline().strip())
    result = 0
    if len(s) != 0:
        while s.count('-') != 0:
            if s[0] == '-':
                tofind = '+'
            else:
                tofind = '-'
            try:
                index = s.index(tofind)
            except:
                index = len(s)
            for i in xrange(index):
                s[i] = tofind
            result += 1
            # print s, result



    print 'Case #{0}: {1}'.format(case, result)

