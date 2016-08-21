case = int(raw_input())
for c in xrange(1,case+1):
    ans = 'impossible' 
    n = int(raw_input())
    if n == 0:
        print "Case #%d: INSOMNIA"%c
    else:
        digit_check = [False for i in range(10)]
        i = 1
        while True:
            s = str(n * i)
            for d in s:
                digit_check[int(d)] = True

            if reduce(lambda x, y: x and y, digit_check):
                print "Case #%d: %s"%(c, s)
                break

            i += 1

            if i > 100000:
                break
