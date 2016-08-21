t = int(raw_input())

for tn in xrange(1, t+1):
    inp_stack = raw_input()
    n = 0

    state = inp_stack[0]

    for pancake in inp_stack:
        if pancake != state:
            n+=1
            state = pancake

    if state is "-":
        n += 1 

    print "Case #{}: {}".format(tn, n)