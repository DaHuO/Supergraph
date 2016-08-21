file = open('B-large.in', 'r')
output = open('B-large.ou', 'w')

T = file.readline()
i = 1
for pancakes_pile in file:
    pancakes_pile = pancakes_pile.rstrip()

    curr_pancake = pancakes_pile[0]
    n_groups = 1

    for pancake in pancakes_pile[1:]:
        if pancake != curr_pancake:
            n_groups += 1
            curr_pancake = pancake

    res = n_groups - 1 if (pancakes_pile[-1] == '+') else n_groups

    print('Case #' + str(i) + ': ' + str(res))
    output.write('Case #' + str(i) + ': ' + str(res) + '\n')
    i += 1

output.close()
