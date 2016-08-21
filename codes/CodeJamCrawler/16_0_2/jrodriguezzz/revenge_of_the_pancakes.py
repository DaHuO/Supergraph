def last_blank_side(li):
    try:
        return (len(li) - 1) - li[::-1].index('-')
    except ValueError:
        return -1

t = int(raw_input())
for i in xrange(1, t + 1):
    pile = list(raw_input())
    iterations = 0
    last_blank_side_pos = last_blank_side(pile)
    while (last_blank_side_pos > - 1):
        for j in xrange(last_blank_side_pos + 1):
            pile[j] = "-" if pile[j] == "+" else "+"   
        iterations += 1
        last_blank_side_pos = last_blank_side(pile)
    print "Case #{}: {}".format(i, iterations)
