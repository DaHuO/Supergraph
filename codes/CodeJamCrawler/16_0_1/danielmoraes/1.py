t = int(raw_input())

for i in xrange(1, t + 1):
    n = int(raw_input())

    digits = [0] * 10
    found_digits = 0

    if n == 0:
        c_n = "INSOMNIA"
    else:
        j = 1
        while (found_digits < 10):
            c_n = n * j
            for d in str(c_n):
                if (digits[int(d)] == 0):
                    digits[int(d)] = 1
                    found_digits += 1
            j += 1

    print "Case #{}: {}".format(i, c_n)
