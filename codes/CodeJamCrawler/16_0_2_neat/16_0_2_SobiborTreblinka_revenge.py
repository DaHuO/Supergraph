import sys

f = open(sys.argv[1], 'r')

for case in range(0, int(f.readline())):
    array = list(f.readline().rstrip())

    index = 0
    count = 0
    length = len(array)

    while index < length:
        char = array[index]

        if index == length - 1:
            if char == '-':
                count += 1
        else:
            next = array[index + 1]
            if char != next:
                count += 1

        index += 1

    print 'Case #{}: {}'.format(case + 1, count)

    case += 1