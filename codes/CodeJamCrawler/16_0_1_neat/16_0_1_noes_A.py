cases = input()

for test in range(cases):
    N = input()


    if N == 0:
        print "Case #%d: INSOMNIA" % (test+1)
        continue

    D = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    naming = N
    while True:
        strnaming = str(naming)
        for digit in strnaming:
            D[int(digit) - int('0')] = 1

        feas = True
        for i in range(10):
            if D[i] == 0:
                feas = False
        if feas == True:
            print "Case #%d: %d" % (test+1, naming)
            break

        naming += N

