def Counting(n):
    if n==0:
        return 'INSOMNIA'
    set_num = set([0,1,2,3,4,5,6,7,8,9])

    multiple = 1

    while 1:
        cur = str(multiple*n)
        for i in cur:
            tmp = int(i)
            if tmp in set_num:
                set_num.remove(tmp)
        if not set_num:
            return cur
            break
        else:
            multiple += 1



t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    print "Case #%d: %s"%(i+1, Counting(n))