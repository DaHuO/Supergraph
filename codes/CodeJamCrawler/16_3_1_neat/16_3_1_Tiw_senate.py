import operator


def sum_list(l):
    s = 0
    for nl in l:
        s += nl[1]
    return s


def check_major(l):
    ss = sum_list(l)
    #print l
    for nl in l:
        if ss > 0:
            if float(nl[1])/ss > 0.5:
                return False
    return True


f = open('A-large.in.txt')
cases = int(f.readline())
#print cases
for i in range(0, cases):
    d = []
    p = int(f.readline())
    print 'Case #%d:' % (i+1),
    ll = f.readline().replace('\n', '').replace('\r', '').split(' ')
    for j in range(0, p):
        d.append(['%s' % chr(ord('A')+j), int(ll[j])])
    d = sorted(d, key=operator.itemgetter(1), reverse=True)

    #print d
    while sum_list(d) > 0:
        ff = d[0]
        ll = d[1]
        if sum_list(d) % 2 == 0:
            if ll[1] > 0:
                print '%s%s' % (ff[0], ll[0]),
                ff[1] -= 1
                ll[1] -= 1
                #print check_major(d)
            else:
                print '%s%s' % (ff[0], ff[0]),
                ff[1] -= 2
                #print check_major(d)
        else:
            print '%s' % (ff[0]),
            ff[1] -= 1
        d = sorted(d, key=operator.itemgetter(1), reverse=True)
        #print d
    print ''
