test_cases = int(raw_input())
counter = 1


def beatrix_sleeper(N, imutN):
    tmp = N
    recurse_flag = False
    if tmp == 0:
        print 'INSOMNIA'
        return

    while tmp is not 0:
        # print "26"
        if digit_flags[tmp % 10] == 0:
            digit_flags[tmp % 10] = 1
            # print "28"1
        tmp /= 10

    for k in digit_flags:
        if digit_flags[k] == 1:
            continue
        else:
            recurse_flag = True
            break
    if recurse_flag:
        global counter
        counter += 1
        beatrix_sleeper(counter * imutN, imutN)
    else:
        print N


for t in xrange(test_cases):
    counter = 1
    digit_flags = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
    }
    N = int(raw_input())
    print "Case #%s:" % str(t + 1),
    beatrix_sleeper(N, N)
