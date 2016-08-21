
num_test = int(raw_input())
for test_case in xrange(1,num_test+1):

    input  = raw_input()
    res = ""
    for c in input:
        if not res or c >= res[0]:
            res = c + res
        else:
            res += c

    print "Case #{}: {}".format(test_case, res)