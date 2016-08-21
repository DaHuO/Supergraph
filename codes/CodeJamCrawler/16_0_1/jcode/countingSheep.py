__author__ = 'jcode'

def all_nums(d):
    return all(d.values())


def check_nums(N, num_dict, i=1):
    for num in list(str(N*i)):
        num_dict[num] = True

    if all_nums(num_dict):
        return N*i
    else:
        return check_nums(N, num_dict, i+1)

# print check_nums(1, d)

num_tests = int(raw_input())
for x in xrange(1, num_tests+1):
    d = {'0': False, '1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False, '8': False, '9': False}
    N = raw_input()
    try:
        if N == '0':
            ret = "INSOMNIA"
        else:
            ret = check_nums(int(N), d)
    except RuntimeError:
        ret = "INSOMNIA"
    print "Case #{}: {}".format(x, ret)



