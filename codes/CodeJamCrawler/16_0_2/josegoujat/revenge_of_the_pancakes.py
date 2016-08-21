# Read problem
no_of_cases = int(raw_input())
cases = []
for i in range(no_of_cases):
    cases.append(raw_input())

# Iterate cases
for i, case in enumerate(cases):
    no_of_pancake_groups = 1
    current_pancake_group_state = case[0]

    # Iterate over the stack of pancakes to calculate same sided groups
    for pancake in case:
        if pancake != current_pancake_group_state:
            no_of_pancake_groups += 1
            current_pancake_group_state = pancake

    # Calculate number of flip movements needed
    times_to_flip = None
    if case[-1] == '-':
        times_to_flip = no_of_pancake_groups
    elif case[-1] == '+':
        times_to_flip = no_of_pancake_groups - 1

    print "Case #{}: {}".format(i+1, times_to_flip)
