__author__ = 'sumant'


def get_unique_digits(num):
    ret = set()
    while num > 0:
        ret.add(num % 10)
        num /= 10
    return ret


def get_last_num(start):
    if start == 0:
        return 'INSOMNIA'
    nums_left = set([_x for _x in range(10)])
    num = start
    while True:
        digits = get_unique_digits(num)
        nums_left.difference_update(digits)
        if len(nums_left) == 0:
            break
        num += start
    return num

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        N = int(raw_input())
        print 'Case #%s: %s' % (i+1, get_last_num(N))
