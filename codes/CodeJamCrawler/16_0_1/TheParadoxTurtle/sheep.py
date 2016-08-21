with open("A-large.in") as f:
    T = int(f.readline())
    for t in range(T):
        N = int(f.readline())
        if N == 0:
            print "Case #" + str(t+1) + ": INSOMNIA"
            continue
        digits = {}
        val = N
        tot = 1
        dig = str(val)
        for d in dig:
            if d not in digits:
                digits[d] = 1

        while len(digits) < 10:
            val += N
            tot += 1
            dig = str(val)
            for d in dig:
                if d not in digits:
                    digits[d] = 1

        print "Case #" + str(t+1) + ": " + str(val)


