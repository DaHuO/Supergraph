t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())  # read a list of integers, 2 in this case
    max_ = 10 ** (len(str(n)) + 1)
    flag = False
    iden = [0] * 10
    sum = 0
    last = "INSOMNIA"
    for i1 in range(1, max_):
        temp = i1 * n
        for j in str(temp):
            j1 = int(j)
            if iden[j1] == 0:
                iden[j1] = 1
                sum += 1
            if sum == 10:
                flag = True
                last = str(temp)
                break
        if flag == True:
            print "Case #{}: {}".format(i, last)
            break
    if flag == False:
        print "Case #{}: {}".format(i, last)


  # check out .format's specification for more formatting options