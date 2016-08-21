def flip_pancakes(pancake_sides):
    
    prev_side = pancake_sides[0]
    pos = 1
    num_flips = 0

    while "-" in pancake_sides or pos <= len(pancake_sides)-1:

        if prev_side == '-' and pos == len(pancake_sides):
            pancake_sides = flip(pos-1, pancake_sides)
            num_flips += 1
            pos += 1

        elif pancake_sides[pos] == prev_side:
            pos += 1


        elif pancake_sides[pos] == '-' and prev_side == '+':
            pancake_sides = flip(pos-1, pancake_sides)
            prev_side = '-'
            pos+=1
            num_flips += 1

        elif pancake_sides[pos] == '+' and prev_side == '-':
            pancake_sides = flip(pos-1, pancake_sides)
            prev_side = '+'
            pos+=1
            num_flips += 1


    return num_flips


def flip(flipping_position, pancake_sides):
    pancake_list = list(pancake_sides)

    for i in range(0, flipping_position+1):
        if pancake_list[i] == '-':
            pancake_list[i] = '+'

        else:
            pancake_list[i] = '-'

    flipped_pancakes = ''.join(pancake_list)

    return flipped_pancakes


num_testcases = int(raw_input())  # read a line with a single integer
for i in xrange(1, num_testcases + 1):
    pancake_string = raw_input()  # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    print "Case #{}: {}".format(i, flip_pancakes(pancake_string))








