test_cases = input()

pre_set = set([0,1,2,3,4,5,6,7,8,9])

for  i in range(1,test_cases+1):
    N = input()

    if N == 0:
        print 'Case #' + str(i) + ': INSOMNIA'

    else:
        j = 1
        temp = N
        answer_set = set([])
        while(True):
            for n in str(temp):
                answer_set.add(int(n))

            if answer_set == pre_set:
                print 'Case #' + str(i) + ': ' + str(temp)
                break

            j = j + 1
            temp = N*j






