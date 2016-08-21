import sys

def has_digit(number, digit):
    return str(digit) in str(number)

def inf_range():
    i = 1
    while True:
        yield i
        i += 1

def delx(number, not_found):
    return [x for x in not_found if not has_digit(number, x)]

def calculate(N):
    if N == 0:
        return 'INSOMNIA'
    else:
        not_found = range(0, 10)
        for i in inf_range():
            num = i * N
            not_found = delx(num, not_found)
            if len(not_found) == 0:
                return num

for i in range(1, int(sys.stdin.readline()) + 1):
    N = int(sys.stdin.readline())
    print('Case #%d: %s' % (i, str(calculate(N))))
