def sheep(n):
    hash = [0]*10
    curr_num = 0
    save_num = 0
    for i in xrange(1,1000000):
        save_num = curr_num = n*i
        while curr_num > 0:
            q = curr_num % 10
            curr_num = curr_num // 10
            hash[q] += 1
        if 0 not in hash:
            return save_num
    return -1


t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    ret = sheep(n)
    if ret == -1:
        print "Case #%d: INSOMNIA" % (i)
    else:
        print "Case #%d: %d" %(i,ret)
