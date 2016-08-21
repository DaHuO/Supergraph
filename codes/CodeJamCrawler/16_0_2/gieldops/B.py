def flip(stack, number):
    new_stack = [1] * len(stack)
    for i in xrange(len(stack)):
        if i < number:
            new_stack[number-i-1] = 1 - stack[i]
        else:
            new_stack[i] = stack[i]
    return new_stack

t = int(raw_input())
for case in xrange(1, t + 1):
    s = raw_input()
    nb_pancakes = len(s)
    stack = [1] * nb_pancakes
    for i, p in enumerate(s):
        stack[i] = 1 if p == "+" else 0

    if not 0 in stack:
        print "Case #%d: 0" % case
        continue

    if not 1 in stack:
        print "Case #%d: 1" % case
        continue

    nb_flips = 0
    while 0 in stack:
        # print stack
        last_plus = 0
        while stack[-last_plus-1] != 0:
            last_plus += 1
        last_plus = nb_pancakes - last_plus

        if last_plus == 0:  # xxxx-
            if stack[0] == 0:  # -xxx-
                stack = flip(stack, nb_pancakes)  # +xxx+
                nb_flips += 1
            else:              # +xxx-
                first_plus = 0
                while stack[first_plus] == 0:
                    first_plus += 1
                stack = flip(stack, first_plus + 1)
                nb_flips += 1
        else:
            # maak minnekes t.e.m. die last_plus
            if stack[0] == 0:  # -xxx+
                stack = flip(stack, last_plus)
                nb_flips += 1
            else:  # +xxx+
                first_plus = 0
                while stack[first_plus+1] == 1:
                    first_plus += 1
                stack = flip(stack, first_plus + 1)
                nb_flips += 1
        
    print "Case #%d: %d" % (case, nb_flips)