__author__ = 'khaleeque'


def count_sheep(num):
    if num==0:
        return 'INSOMNIA'

    all_digits = set('0123456789')

    digits_covered = set()

    for i in xrange(1,1000000):
        digits_covered = digits_covered.union(set(str(num*i)))
        if digits_covered == all_digits:
            # print num*i
            return str(num*i)
            break


def min_maneuvers(inp_str):

    if inp_str == '':
        return 0
    elif inp_str == '+':
        return 0
    elif inp_str == '-':
        return 1
    elif inp_str == '++':
        return 0
    elif inp_str == '-+':
        return 1
    elif inp_str == '--':
        return 1
    elif inp_str == '+-':
        return 2
    else:
        part1 = inp_str[:2]
        part2 = '+'+inp_str[2:]
        return min_maneuvers(part1) + min_maneuvers(part2)


def str_compacter(inp_str):
    if inp_str == '':
        return ''
    to_return = inp_str[0]
    for c in inp_str[1:]:
        if to_return[-1] == c:
            pass
        else:
            to_return+=c
    return to_return

if __name__ == '__main__':
    with open('temp_input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
    t = int(lines[0])
    lines = lines[1:]
    # exit()
    # t = input()c
    for i in xrange(len(lines)):
        # n = input()
        print "Case #"+str(i+1)+":", min_maneuvers(str_compacter(lines[i]))