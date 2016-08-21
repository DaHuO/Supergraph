t = int(raw_input())

for i in range(1, t+1):
    n = int(raw_input())
    if n == 0:
        print "Case #%d: INSOMNIA" % i
    else:
        h = [False] * 10
        count = 0
        nn = n
        while True:
            for c in str(nn):
                ic = int(c)
                if not h[ic]:
                    h[ic] = True
                    count += 1
                    if count == 10:
                        break
            if count == 10:
                break
            else:
                nn += n
        print "Case #%d: %d" % (i, nn)
