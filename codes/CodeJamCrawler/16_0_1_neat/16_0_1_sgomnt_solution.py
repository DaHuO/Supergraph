import sys


def multi(n, k, digits):
    m = str(n * k)
    for char in m:
        if char in digits:
            digits.pop(digits.index(char))
    if n == 0:
        return 'INSOMNIA'
    if digits != []:
        return multi(n, k + 1, digits)
    else:
        return m

n_cases = int(sys.stdin.readline())


for i in range(n_cases):
    number = int(sys.stdin.readline())
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print 'Case #' + str(i + 1) + ":", multi(number, 1, digits)