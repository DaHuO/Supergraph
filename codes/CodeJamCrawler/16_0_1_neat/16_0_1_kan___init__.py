import sys


def count_sheep(num):
    checkpoint = [0 for i in xrange(0, 10)]
    if num == 0:
        return 'INSOMNIA'
    index = 1
    while 1:
        count = str(num*index)
        #print '{} result = {}'.format(num, count)
        for i in count:
            checkpoint[int(i)] = 1
        #print 'sum point = {}'.format(sum(checkpoint))
        if sum(checkpoint) == 10:
            return count
        index += 1


with open(sys.argv[1], 'r') as f:
    input = [line for line in f]
    num_case = input[0]
    del input[0]
    count_list = [count_sheep(int(line)) for line in input]
    case = 1
    for i in count_list:
        print 'Case #{}: {}'.format(case, i)
        case += 1
