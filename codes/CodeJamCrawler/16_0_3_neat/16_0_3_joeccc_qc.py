import math


def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


def get_divisor(n):
    # max_try = int(math.floor(math.sqrt(n)))
    max_try = 10
    for k in range(2, max_try + 1):
        if n % k == 0:
            return k
    return None


def num_of_base_x(n, x):
    if len(n) > 0:
        return num_of_base_x(n[:len(n) - 1], x) * x + num(n[-1:])
    else:
        return 0


def to_base_2(n):
    if n == 1:
        return '1'
    else:
        return to_base_2(n / 2) + str(n % 2)


# print to_base_2(17)
# print num_to_base_x('1010', 9)
f = open('qc.test')

count = num(f.readline())

for i in range(1, count + 1):

    print 'Case #{}:'.format(i)

    pair = f.readline()
    nj = pair.split(' ')
    n, j = int(nj[0]), int(nj[1])

    num_in_test = '1' + '0' * (n - 2) + '1'
    while j > 0:
        results = []
        for base in range(2, 11):
            divisor = get_divisor(num_of_base_x(num_in_test, base))
            if divisor is not None:
                results.append(str(divisor))
            else:
                break
        if len(results) == 9:
            j -= 1
            print '{} {}'.format(num_in_test, ' '.join(results))
        num_in_test = to_base_2(num_of_base_x(num_in_test, 2) + 2)

