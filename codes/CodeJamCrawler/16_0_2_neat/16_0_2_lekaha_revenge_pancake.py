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


def load_input(filename = None):
    if not filename:
        return
    line_buffer = None
    with open(filename, 'r+') as f:
        line_buffer = f.read().splitlines()
    f.close()
    return line_buffer


import sys

def main(argv):
    if not argv:
        filename = __file__
        lines = ['1', '--+-']
    else:
        filename = argv[0]
        lines = load_input(filename + '.in')
    f = open(filename + '.out', 'w+')
    print int(lines[0]) == (len(lines) - 1)
    for i in xrange(int(lines[0])):
        flip_list = list(lines[i + 1])
        flip_times = flip_pancake(flip_list)
        s = 'Case #%d: %d\n' % (i + 1, flip_times)
        f.write(s)
        print '%s' % s

    f.close()


if __name__ == '__main__':
    main(sys.argv[1:])