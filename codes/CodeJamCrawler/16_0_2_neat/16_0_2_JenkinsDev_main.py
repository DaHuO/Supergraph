num_tests = int(raw_input())

def all_happy(cur_l):
    return not '-' in list(cur_l)

def rindex(needle, haystack):
    return len(haystack) - haystack[::-1].index(needle)

def swap_list(cur_l):
    return ['+' if l == '-' else '-' for l in cur_l]

for i in range(1, num_tests + 1):
    cur_l = inp = list(raw_input())
    val = 0
    while not all_happy(cur_l):
        ind_of_last = rindex('-', cur_l)
        cur_l = list(swap_list(cur_l[:ind_of_last])) + cur_l[ind_of_last:]
        val += 1
    print('Case #%s: %s' % (i, val))
