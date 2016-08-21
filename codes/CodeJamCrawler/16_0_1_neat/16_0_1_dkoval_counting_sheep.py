from sys import stdin


def read_input():
    cases = int(stdin.readline())  # ignore number of cases
    nums = []
    while cases:
        nums.append(int(stdin.readline()))
        cases -= 1
    return nums


def mult(value, digit):
    for i in xrange(1, 200):
        n = i * value
        while n:
            if n % 10 == digit:
                return i
            n /= 10
    return -1


def max_factor(value):
    if not value:
        return 0
    max_f = 0
    for i in xrange(10):
        max_f = max(max_f, mult(value, i))
    return max_f


if __name__ == '__main__':
    for idx, num in enumerate(read_input()):
        result = 0
        if num:
            result = max_factor(num)
        if result <= 0:
            result = 'INSOMNIA'
        else:
            result = str(result * num)
        print 'Case #%d: %s' % (idx + 1, result)
