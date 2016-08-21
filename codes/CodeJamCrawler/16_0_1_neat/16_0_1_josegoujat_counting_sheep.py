# Read problem
no_of_cases = int(raw_input())
cases = []
for i in range(no_of_cases):
    cases.append(int(raw_input()))

# Iterate cases
for j, case in enumerate(cases):
    # Special case
    if case == 0:
        print "Case #{}: INSOMNIA".format(j+1)
        continue

    # Init variables
    have_appeared = [False for i in range(10)]
    i = 1
    naming = None

    # Loop until all digits are found
    while not all(have_appeared):
        naming = i * case
        digits = set([int(d) for d in str(naming)])
        for d in digits:
            have_appeared[d] = True

        i += 1

    print "Case #{}: {}".format(j+1, naming)
