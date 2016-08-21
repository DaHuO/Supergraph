import math


def get_first_non_trivial_divisor(number):
    root = int(math.sqrt(number))
    for x in xrange(2, root + 1):
        if number % x == 0:
            return x
    return -1

def generate(n):
    number = n - 2
    for x in xrange(number ** 2):
        yield "1{:0>{width}b}1".format(x, width=n-2)

def different_bases(x):
    return [int(x, base) for base in xrange(2, 11)]

for case_num in xrange(int(raw_input())):
    n, j = [int(val) for val in raw_input().split()]
    count = 0

    print 'Case #{}:'.format(case_num + 1)
    for x in generate(n):
        tmp = [x]
        flag = True
        for base in different_bases(x):
            tmp.append(get_first_non_trivial_divisor(base))
            if tmp[-1] == -1:
                flag = False
                break

        if flag:
            print ' '.join(map(str, tmp))
            count += 1

        if count == j:
            break


