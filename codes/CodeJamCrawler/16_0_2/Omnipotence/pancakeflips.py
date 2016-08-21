import sys


def main(argv):
    # read in file
    input_file = argv[0]
    f = open(input_file)
    T = int(f.readline())
    for i in xrange(1, T+1):
        case = f.readline().rstrip('\n')
        print "Case #%s: %s" % (i, calculate(case))


def calculate(case):
    if case == len(case) * '+':
        return 0
    seen_states = set([case])
    n_flips = 1
    while True:
        new_states = []
        for state in seen_states:
            for i in xrange(1, len(case) + 1):
                new_state = flip(i, state)
                if new_state == len(case) * '+':
                    return n_flips
                elif new_state not in seen_states:
                    new_states.append(new_state)
        seen_states |= set(new_states)
        n_flips += 1


def flip(n, stack):
    stack_list = list(stack)
    to_flip = stack_list[:n]
    leave = stack_list[n:]
    flipped = ['+' if pancake == '-' else '-' for pancake in to_flip]
    flipped.reverse()
    return ''.join(flipped + leave)

if __name__ == '__main__':
    main(sys.argv[1:])
