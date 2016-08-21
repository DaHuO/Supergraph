n = int(raw_input())
for itt in xrange(n):
    num = int(raw_input())
    # solving the problem
    if num == 0:
        print 'Case #' + str(itt + 1) + ': INSOMNIA'
        continue
    covered = [False] * 10
    curr_num = 0
    while not all(covered):
        curr_num += num
        for d in str(curr_num): covered[int(d)] = True
    print 'Case #' + str(itt + 1) + ': ' + str(curr_num)
