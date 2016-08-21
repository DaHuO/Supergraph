#
# codejam contest
# https://code.google.com/codejam/contest/6254486/dashboard
#
def build_list():
    num_list = ['0', '1', '2', '3',
                '4', '5', '6', '7',
                '8', '9']
    return num_list

def read_file(filename):
    with open(filename) as fd:
        input_list = fd.read().splitlines()

    return input_list



def count_sheep(max_N, N, num_list):
    if N == 0:
        return 'INSOMNIA'

    sheep_list = num_list[:]

    for i in range(1, max_N+1):
        counts = i*N
        for c in str(counts):
            if c in sheep_list:
                sheep_list.remove(c)
            elif not sheep_list: # list empty
                return str(counts)
        if not sheep_list: # list empty
            return str(counts)

    return 'INSOMNIA'


import sys

def main(argv):
    if not argv:
        print "Enter filename."
        sys.exit()

    num_list = build_list()
    filename = argv[0]
    input_list = read_file(filename + '.in')
    f = open(filename + '.out', 'w+')

    T = int(input_list[0]) # the number of cases

    for t in range(1, T+1):
        max_N = 200
        last_n = count_sheep(max_N, int(input_list[t]), num_list)

        s = 'Case #%d: %s\n' % (t, last_n)
        f.write(s)
        print '%s' % s

    f.close()


if __name__ == '__main__':
    main(sys.argv[1:])
