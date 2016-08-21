T = int(input())
for tid in range(1, T+1):
    N = int(input())
    a = [int(x) for x in input().split(' ')]
    aa = [x for x in a]
    #print(a)
    sucet = 0
    for i in range(0, N):
        sucet += a[i]
    v = []
    while (sucet > 0):
        #print(a)
        max1 = 0
        ind1 = 0
        for i in range(0, N):
            if (a[i] > max1):
                max1 = a[i]
                ind1 = i
        max2 = 0
        ind2 = 0
        for i in range(0, N):
            if (a[i] > max2) and (i != ind1):
                max2 = a[i]
                ind2 = i

        rozne = 0
        for i in range(0, N):
            if (a[i] > 0):
                rozne+= 1

        if ((max1 != max2) or (rozne > 2)):
            v.append(chr(ord('A')+ind1))
            a[ind1] -= 1
            sucet -= 1
        else:
            v.append(chr(ord('A')+ind1)+chr(ord('A')+ind2))
            a[ind1]-=1
            a[ind2] -= 1
            sucet -= 2
        #print(ind)
    #    maximum = -1
    #    ss = 0
    #    for i in range(0, N):
    #        ss += a[i]
    #        if (a[i] > maximum):
    #            maximum = a[i]
    #    if (2*maximum > ss):
    #        print('cele zle', N, aa)
    print('Case #{}: {}'.format(tid," ".join(v)))
