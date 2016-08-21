import sys


def int_to_digit_set(n):
    int_str = str(n)
    int_list = [int(i) for i in int_str]
    return set(int_list)


def count_sheep(n):
    if n == 0:
        return 'INSOMNIA'

    seen_digits = int_to_digit_set(n)
    i = 1
    while seen_digits != set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        xn = i*n
        seen_digits = seen_digits.union(int_to_digit_set(xn))
        i += 1

    #print 'N %s after %s iterations' % (str(n), str(i-1))
    return xn


if __name__ == "__main__":

    out_file = open('out.txt','w')
    in_file = open(sys.argv[1],'r')
    in_file.readline()
    case = 1
    for line in in_file:
        n = int(line)
        result = count_sheep(n)
        out_file.write('Case #%s: %s\n' % (str(case), str(result)))
        case += 1