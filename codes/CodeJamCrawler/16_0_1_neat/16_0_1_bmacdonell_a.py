import sys


def evaluate(n):
    if n == 0:
        return 'INSOMNIA'
    digits = set('0123456789')
    i = 0
    while digits:
        i += 1
        for digit in str(i * n):
            if digit in digits:
                digits.remove(digit)
    return i * n


if __name__ == '__main__':
    _ = sys.stdin.readline()  # skip count of test cases
    for i, line in enumerate(sys.stdin.readlines()):
        n = int(line)
        result = evaluate(n)
        print 'CASE #{0}: {1}'.format(i + 1, result)
