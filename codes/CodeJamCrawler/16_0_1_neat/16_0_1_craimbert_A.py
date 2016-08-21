def read_int():
    return int(raw_input())

def int_to_array_of_ints(num):
    return map(int, str(num))

def diff_lists(list1, list2):
    return list(set(list1) - set(list2))

def infinite_cond(num, multiplicator):
    no_progress = num == N and multiplicator > 1
    overflow = max_multiple_seen > 9223372036854775807
    infinite_cond = no_progress or overflow
    return infinite_cond

DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

_T = read_int()  # nbr of test cases
for _t in range(_T):
    N = read_int()
    # print("Begin: N = %d" % N)
    max_multiple_seen = N
    multiplicator = 1
    not_seen_digits = DIGITS
    infinite = False

    while not_seen_digits:
        max_multiple_seen = multiplicator * N
        if infinite_cond(max_multiple_seen, multiplicator):
            infinite = True
            break
        # print("Multiple=%d : N=%d times %d" % (max_multiple_seen, N, multiplicator))
        tmp_int_array = int_to_array_of_ints(max_multiple_seen)
        not_seen_digits = diff_lists(not_seen_digits,tmp_int_array)
        # print("Unseen digits are now: %s" % not_seen_digits)

        multiplicator+=1

    if infinite:
        print "Case #%d: %s" % (_t+1, 'INSOMNIA')
    else:
        print "Case #%d: %d" % (_t+1, max_multiple_seen)

