__author__ = 'morgana'


def flip_pancakes(pancakes):
    i = len(pancakes) - 1
    flip_counts = 0
    while i >= 0:
        if pancakes[i] == '-':
            to_flip = pancakes[0:i+1]
            flipped = ''
            for c in to_flip:
                if c == '-':
                    c = '+'
                else:
                    c = '-'
                flipped = '{}{}'.format(flipped, c)
            pancakes = '{}{}'.format(flipped, pancakes[i+1:])
            flip_counts += 1
        # else:
        #    new_stack = '+{}'.format(new_stack)
        i -= 1
    #print pancakes
    return flip_counts

if __name__ == '__main__':
    f = open('B-large.in')
    case_count = int(f.readline())

    cases = list()
    g = open('out.txt', 'w')
    for case_number in xrange(case_count):
        case = f.readline().strip()
        g.writelines('Case #{}: {}\n'.format(case_number+1, flip_pancakes(case)))
    g.close()
    f.close()
