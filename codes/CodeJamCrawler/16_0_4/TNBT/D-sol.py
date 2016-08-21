for _ in range(int(input())):
    K, C, S = map(int, raw_input().split(' '))
    print('Case #{}:'.format(_+1)),
    if K == 1:
        print 1
        continue
    if K==S:
        for i in range(1,K+1):
            if C != 1 and i == 1:
                continue
            print i,
        print ''
        continue
    else:
        if C == 1 or K > S+1:
            print 'IMPOSSIBLE'
        else:
            for i in range(1,K+1):
                if C != 1 and i == 1:
                    continue
                print i,
        print ''
        continue