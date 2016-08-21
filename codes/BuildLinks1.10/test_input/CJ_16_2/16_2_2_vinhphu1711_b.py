T = int(raw_input())

def test(n1, n2):
    #print n1, n2
    for i in range(len(n2)):
        #print i
        if n2[i] != '?' and n1[i] != n2[i]:
            return False
    return True

for t in range(T):
    C, J = raw_input().split()
    
    l = len(C)
    if l == 1:
        pattern = '%01d'
    elif l == 2:
        pattern = '%02d'
    else:
        pattern = '%03d'

    L = 10**l

    min_diff = 99999
    res_C, res_J = 99999, 99999
    for c in xrange(L):
        if not test(pattern % c, C):
            continue
        for j in xrange(L):
            if not test(pattern % j, J):
                continue
            diff = abs(c-j) 
            if diff < min_diff:
                min_diff = diff
                res_C = c
                res_J = j
            elif diff == min_diff:
                if c < res_C:
                    res_C = c
                    res_J = j
                elif c == res_C:
                    if j < res_J:
                        res_J = j
    
    #print min_diff
    #res_C, res_J = 0, 0

    print 'Case #%d: %s %s' % (t+1, pattern % res_C, pattern % res_J)