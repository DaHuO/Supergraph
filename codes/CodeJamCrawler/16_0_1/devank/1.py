
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    if n == 0:
        print "Case #{}: INSOMNIA".format(i)
    else:
        digits = [0,1,2,3,4,5,6,7,8,9]
        mult = 1
        cal_n = n
        while len(digits):
            cal_n = n * mult
            while cal_n:
                n_digit = cal_n % 10
                for j in xrange(0, len(digits)):
                    if n_digit == digits[j-1]:
                        del digits[j-1]
                cal_n //= 10
            mult = mult + 1
        print "Case #{}: {}".format(i, n * (mult-1))