def to_digits(n):

    n_str = str(n)
    n_list = [int(i) for i in n_str]

    return set(n_list)


def last_num(n):

    int_list = [0,1,2,3,4,5,6,7,8,9]
    if n == 0:
        return "INSOMNIA"
    factor = 1
    while len(int_list)>0:
        val = n*factor
        digits = to_digits(val)
        clone_list = int_list[:]
        for num in clone_list:
            if num in digits:
                int_list.remove(num)
                if len(int_list)==0:
                    return val
        factor += 1
    return val


t = int(raw_input())

for i in xrange(1, t + 1):
    n = int(raw_input())
    print "Case #{}: {}".format(i, last_num(n))
