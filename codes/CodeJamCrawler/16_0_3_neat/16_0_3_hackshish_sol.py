#!/usr/bin/python

def func(N , J):
    import math
    import itertools
    temp = ["".join(seq) for seq in itertools.product("01", repeat=N-2)]
    all_c = ['1' + elem + '1' for elem in temp]
    bases = [2,3,4,5,6,7,8,9,10]
    for s_num in all_c:
        p_flag = False
        l_div = [None] * 9
        for ind, base in enumerate(bases):
            n = int(s_num, base)
            if n % 2 == 0:
                l_div[ind] = str(2)
                continue
            for divisor in xrange(3, int(math.sqrt(n)) + 1, 2):
                if n % divisor == 0:
                    l_div[ind] = str(divisor)
                    break
            if l_div[ind] == None:
                p_flag = True
                break

        if not p_flag:
            print s_num + ' ' + ' '.join(l_div)
            J -= 1
        if J == 0:
            return

t = int(raw_input())
for i in xrange(1, t + 1):
    # print "Case #{}: {}".format(i, func(raw_input()))
    N, J = map(int, raw_input().split(' '))
    print 'Case #' + str(i) + ':'
    func(N, J)
