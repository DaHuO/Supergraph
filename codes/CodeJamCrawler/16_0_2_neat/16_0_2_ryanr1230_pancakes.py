T = int(raw_input())
for i in range(T):
    pancakes = list(raw_input())
    end_it = len(pancakes)
    want_char = '+'
    num_flips = 0
    while end_it > 0:
        end_it -= 1
        if pancakes[end_it] == want_char:
            continue
        want_char = pancakes[end_it]
        num_flips += 1
    print "Case #%d: %d" % (i+1, num_flips)
        

