#
# codejam contest
# https://code.google.com/codejam/contest/6254486/dashboard#s=p1
#
def flip_all(a_list):
    r_list = list()
    for i in range(len(a_list)):
        if a_list[i] == '+':
            r_list += '-'
        elif a_list[i] == '-':
            r_list += '+'

    return r_list


def flip_pancake(flip_list):
    if len(flip_list) == 1:
        if flip_list[0] == '+':
            return 0
        elif flip_list[0] == '-':
            return 1

    if flip_list[-1] == '-':
        new_flip_list = flip_all(flip_list[:len(flip_list)-1])
        return flip_pancake(new_flip_list) + 1
    elif flip_list[-1] == '+':
        new_flip_list = flip_list[:len(flip_list)-1]
        return flip_pancake(new_flip_list)


def read_file(filename):
    with open(filename) as fd:
        input_list = fd.read().splitlines()

    return input_list


import sys

def main(argv):
    if not argv:
        print "Enter filename."
        sys.exit()

    filename = argv[0]
    input_list = read_file(filename + '.in')
    f = open(filename + '.out', 'w+')

    T = int(input_list[0]) # the number of cases

    for t in range(1, T+1):
        flip_list = list(input_list[t])

        flip_times = flip_pancake(flip_list)

        s = 'Case #%d: %d\n' % (t, flip_times)
        f.write(s)
        print '%s' % s

    f.close()


if __name__ == '__main__':
    main(sys.argv[1:])
