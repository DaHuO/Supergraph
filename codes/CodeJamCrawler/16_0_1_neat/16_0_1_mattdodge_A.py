def run_case(input):
    N, = read_ints(input)
    digits_seen = set()
    num = 0
    if N == 0:
        return 'INSOMNIA'
    iters = 0
    while iters < 10000:
        num += N
        iters += 1
        digits_seen |= set(str(num))
        if len(digits_seen) >= 10:
            break
    else:
        raise Exception('INSOMNIA?')
    return num

##############################
#    CODE JAM BOILERPLATE    #
##############################


def read_ints(input, n=1):
    """ Read n integers from input - all on one line, space separated """
    return (int(st) for st in read_strs(input, n))


def read_strs(input, n=1):
    """ Read n strings from input - all on one line, space separated """
    return input.readline().rstrip("\n").split(" ")

# GCJ boiler plate...call run_case for each case given
if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10000)
    with sys.stdin as f:
        for case_num in range(int(f.readline())):
            print("Case #%d: %s" % (case_num + 1, run_case(f)))
