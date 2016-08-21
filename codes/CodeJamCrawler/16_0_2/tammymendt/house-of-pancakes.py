import sys


def flip_first_pancakes(pancake_seq):

    side_of_first = pancake_seq[0]

    if side_of_first == '-':
        flipped_side = '+'
    else:
        flipped_side = '-'

    flipped_pancake_seq = ''

    flip = True
    for pancake in pancake_seq:
        if pancake == side_of_first and flip:
            flipped_pancake_seq += flipped_side
        else:
            flipped_pancake_seq += pancake
            flip = False

    return flipped_pancake_seq


def calculate_flips(pancake_seq):

    if '-' in pancake_seq:
        return 1 + calculate_flips(flip_first_pancakes(pancake_seq))
    else:
        return 0

if __name__ == "__main__":

    out_file = open('out.txt','w')
    in_file = open(sys.argv[1],'r')
    in_file.readline()
    case = 1
    for line in in_file:
        result = calculate_flips(line)
        out_file.write('Case #%s: %s\n' % (str(case), str(result)))
        case += 1
