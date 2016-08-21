cases = int(raw_input())


for case in range(1, cases+1):
    line = raw_input().split(' ')
    K = int(line[0])
    C = int(line[1])
    S = int(line[2])

    #if K < S:
    l = []
    for x in range(1, K+1):
        l.append(str(x))
    print 'Case #{}: {}'.format(case,' '.join(l))


    #start = 'L'*K
    #collect = []
    #for x in range(0, K):
    #    collect.append(start[0:x] + 'G' + start[x+1:])
    #print collect
