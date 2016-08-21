tc = input()
for tcn in range(tc):
    n = input()
    sid = set(range(0, 10))
    answer = set([int(i) for i in str(n)])
    if n == 0:
        print 'Case #' + str(tcn+1) + ': INSOMNIA'
    else:
        maxm = 1000000
        for count in range(1, maxm):
            x = n * count
            lst = [int(i) for i in str(x)]
            answer = answer.union(set(lst))
            if sid == answer:
                print 'Case #' + str(tcn+1) + ': ' + str(x)
                break
        if count == maxm:
            print 'Case #' + str(tcn+1) + ': INSOMNIA'
