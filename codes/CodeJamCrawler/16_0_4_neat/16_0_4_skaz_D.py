test_cases = input()

def print_result(t, result):
    print "Case #" + str(t + 1) + ": " + result


def handle_case(t):
    v = raw_input().split()
    T = int(v[0])
    C = int(v[1])
    S = int(v[2])

    # if there is complexity of 1, we need to turn over every stone
    if C == 1:
        if S < T:
            print_result(t, "IMPOSSIBLE")
        else:
            print_result(t, ' '.join(str(x + 1) for x in xrange(0, T)))
    # Otherwise, we can just turn over the all of the stones from the original
    # sequence except the first
    else:
        if T > 1:
            print_result(t, ' '.join(str(x + 1) for x in xrange(1, T)))
        else:
            print_result(t, '1')
for t in range(0, test_cases):
    handle_case(t)


