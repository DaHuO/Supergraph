def least_flips(s):  # We flip maximal blocks of same-side pancakes.
    flips = 0
    current_side = s[0]
    for pancake in s[1:]:
        if pancake != current_side:
            current_side = pancake
            flips += 1
    if current_side == '-':
        flips += 1
    return flips


t = int(raw_input())  # The number of test cases.
for i in xrange(1, t + 1):
    print "Case #{}: {}".format(i, least_flips(str(raw_input())))