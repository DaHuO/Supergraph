for x in xrange(int(raw_input())):
    astr = list(raw_input())
    res = [astr[0]]
    for i in range(1,len(astr)):
        if astr[i] < res[0]:
            res.append(astr[i])
        else:res.insert(0,astr[i])
    print 'Case #'+str(x+1)+':',''.join(res)

