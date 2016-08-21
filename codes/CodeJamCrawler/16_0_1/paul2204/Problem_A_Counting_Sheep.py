import string

def func(num):
    temp = {i:0 for i in range(10)}
    old = {}
    next_num = 0
    while True:
        next_num += num
        if next_num in old:
            return "INSOMNIA"
        tmp_next_num = next_num
        while tmp_next_num  > 0 :
            c = tmp_next_num % 10
            if c in temp:
                del temp[c]
                if len(temp) == 0:
                    return next_num
            tmp_next_num = int(tmp_next_num / 10)
        old[next_num] = 1

t = int(raw_input())
for i in xrange(1, t + 1):
    m = int(raw_input().strip())
    result = func(m)
    print "Case #{}: {}".format(i, result)
