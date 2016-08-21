
test_cases = int(raw_input())

for test_case in xrange(test_cases):

    pancakes = raw_input() + '+'
    swaps = 0

    last_pancake = None
    for pancake in pancakes:
        if last_pancake != pancake:
            swaps += 1
            last_pancake = pancake

    swaps -= 1

    print "Case #" + str(test_case + 1) + ": " + str(swaps)

