def digit_split(n):
    digit_list = map(int, str(n))
    return set(digit_list)

def calculate(n):
    digit = set([0,1,2,3,4,5,6,7,8,9])
    i = 1
    init_n = n
    while True:
        # INFINITE
        if n == 0:
            return "INSOMNIA"
            break

        digit = digit - digit_split(n)
        #print "digit_split : {}, digit : {}".format(digit_split(n), digit)

        if len(digit) == 0:
            return n
            break

        else:
            i += 1
            n = init_n*i

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())  # read a list of integers, 2 in this case
    result = calculate(n)
    print "Case #{}: {}".format(i, result)
    # check out .format's specification for more formatting options

