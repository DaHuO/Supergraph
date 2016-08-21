t = int(raw_input().strip())

for i in xrange(t):
    n = int(raw_input().strip())
    if n == 0:
        print "Case #" + str(i+1) + ": INSOMNIA"
    else:
        digits = set()
        nn = n
        count = 1
    
        while True:
            sn = str(nn)
            for j in xrange(len(sn)):
                digits.add(sn[j])

            if len(digits) == 10:
                break
            count = count + 1
            nn = n * count

        print "Case #" + str(i+1) + ": " + str(nn)
