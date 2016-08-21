t = int(raw_input())

for c in range(t):
    n = int(raw_input())
    if n != 0:
        digits = set(range(0, 10))
        i = 1
        while len(digits) > 0:
            k = i * n
            for d in str(k):
                if int(d) in digits:
                    digits.remove(int(d))
            i += 1
        print "Case #" + str(c+1) + ": " + str(k)
    else:
        print "Case #" + str(c+1) + ": " + "INSOMNIA"
