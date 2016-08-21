__author__ = 'chonnakan'


def check_digit(n, digits):
    num_list = []
    while n > 9:
        e = n % 10
        n /= 10
        num_list.append(e)
        if digits[e] == 0:
            digits[e] = 1
    num_list.append(n)
    if digits[n] == 0:
        digits[n] = 1
    return num_list


def sum_digits(digits):
    sum = 0
    for d in digits:
        sum += d
    return sum


def solve(case, num):
    digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #print num
    if num == 0:
        print 'Case #%d: INSOMNIA'%(i)
    else:
        count = 1
        while sum_digits(digits) != 10 :
            check_digit(count*num, digits)
            count += 1
        count -= 1
        print 'Case #%d: %d'%(i, count*num)


f = open('A-large.in')
cases = int(f.readline())

for i in range(1, cases+1):
    solve(i, int(f.readline()))
