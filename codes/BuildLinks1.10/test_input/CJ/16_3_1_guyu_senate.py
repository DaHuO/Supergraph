t = int(input())

for i in range(t):
    np = int(input()) #number of parties

    s = input().split()
    ml = []
    N = 0
    for j in range(np):
        ml.append([chr(ord('A') + j), int(s[j])])
        N += int(s[j])

    ml.sort(key=lambda x: x[-1], reverse=True)

    print('Case #%d: ' % (i+1), end='')
    while N > 0:
        # print(ml)
        if (len(ml) == 2):
            if (ml[0][1] == ml[1][1]):
                print(ml[0][0] + ml[1][0], end=' ')
                ml[0][1] -= 1
                ml[1][1] -= 1
                if ml[1][1] == 0:
                    ml.pop(1)
                if ml[0][1] == 0:
                    ml.pop(0)
                N -= 2
        else:
            print(ml[0][0], end=' ')
            ml[0][1] -= 1
            if ml[0][1] == 0:
                ml.pop(0)
            N -= 1


        # if (ml[0][1] > ml[1][1] + 1):
        #     print(ml[0][0]*2, end=' ')
        #     ml[0][1] -= 2
        #     N -= 2
        # elif (ml[0][1] > ml[1][1]):
        #     print(ml[0][0], end=' ')
        #     ml[0][1] -= 1
        #     N -= 1
        # else:
        #     print(ml[0][0] + ml[1][0], end=' ')
        #     ml[0][1] -= 1
        #     ml[1][1] -= 1
        #     N -= 2

        # reorder list
        if len(ml) <= 2:
            continue

        p = 1
        q = 2

        while (q < len(ml) and ml[1][1] < ml[q][1]):
            q += 1
        ml.insert(q, ml[1])
        ml.pop(1)

        while (p < len(ml) and ml[0][1] < ml[p][1]):
            p += 1
        ml.insert(p, ml[0])
        ml.pop(0)


    print()
