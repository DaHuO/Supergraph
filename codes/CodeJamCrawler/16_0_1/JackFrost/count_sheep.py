
T = int(input())

for ii in range(1, T+1):
    IN = int(input())
    L = [x for x in range(0,10)]

    if IN == 0:
        print "Case #" + str(ii) + ": INSOMNIA"
    else:

        LOOP = True
        C = 0
        while LOOP:
            C += 1
#            print C
            ARR = [int(i) for i in str(IN*C)]
#            print(ARR)
            Z = []
            for a in L:
                if a in ARR:
                    Z.append(a)

            for a in Z:
                L.remove(a)
            if not L:
                break
        print "Case #" + str(ii) + ": " + str(C*IN)
    
