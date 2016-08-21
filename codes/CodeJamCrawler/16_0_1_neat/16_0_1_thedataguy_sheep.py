T = int(raw_input())

for j in range(1,T+1):
    N = int(raw_input())
    if N != 0:
        noArr = []
        i=1
        while len(noArr) != 10:
            final = N * i
            tempList = list(str(final))
            for k in tempList:
                if k not in noArr:
                    noArr.append(k)
            i = i + 1
        print "Case #{}: {}".format(j,final)
    else:
        print "Case #{}: {}".format(j,'INSOMNIA')
