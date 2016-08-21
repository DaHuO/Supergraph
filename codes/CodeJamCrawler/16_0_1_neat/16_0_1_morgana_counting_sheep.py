__author__ = 'morgana'


def count_sheep(number):
    integers = set()
    for integer in str(number):
        integers.add(integer)
    multiplier = 2
    new_num = 0
    while len(integers) != 10 and new_num != 'INSOMNIA':
        new_num = number * multiplier
        if number == new_num:
            new_num = 'INSOMNIA'
        else:
            for integer in str(new_num):
                integers.add(integer)
        multiplier += 1
    return new_num

if __name__ == '__main__':
    f = open('A-large.in')
    case_count = int(f.readline())

    cases = list()
    g = open('out.txt', 'w')
    for i in xrange(case_count):
        case = int(f.readline().strip())
        g.writelines('Case #{}: {}\n'.format(i+1, count_sheep(case)))
    g.close()
    f.close()
