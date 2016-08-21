import fileinput
import sys


def counting_sheep(N):
    unseen_digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    def helper(n):
        if n == 0:
            return 'INSOMNIA'
        for digit in str(n):
            unseen_digits.discard(digit)
            if not unseen_digits:
                return n
        return None

    i = 1
    ret = helper(N)
    while not ret:
        i += 1
        ret = helper(i * N)

    return ret


if __name__ == '__main__':
    i = 0
    for line in fileinput.input():
        if i > 0:
            y = int(line.strip())
            print 'Case #{}: {}'.format(i, counting_sheep(y))
        i += 1
