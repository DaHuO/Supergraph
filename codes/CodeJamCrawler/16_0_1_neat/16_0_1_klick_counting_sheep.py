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


if __name__ == '__main__':
    with open('temp.txt') as f:
        lines = [int(line.rstrip()) for line in f.readlines()]
    # print lines
    # exit()
    # t = input()
    for i in xrange(100):
        # n = input()
        print "Case #"+str(i+1)+":",count_sheep(lines[i+1])