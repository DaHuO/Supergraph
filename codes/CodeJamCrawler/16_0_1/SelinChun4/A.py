def count_digit(num, digit_lst):
    while num != 0:
        digit = num % 10
        if digit not in digit_lst:
            digit_lst.append(digit)
        num /= 10

    return sorted(digit_lst)

def check_digit(digit_lst):
    for i in range(10):
        if i not in digit_lst:
            return False

    return True

for i in range(int(raw_input())):
    n = int(raw_input())
    digit_lst = []
    digit_lst = count_digit(n, digit_lst)
    insomnia = True

    for j in range(2, 100):
        multiple_n = j * n
        digit_lst = count_digit(multiple_n, digit_lst)
        if check_digit(digit_lst):
            print 'Case #%d: %d' % (i+1, multiple_n)
            insomnia = False
            break

    if insomnia:
        print 'Case #%d: INSOMNIA' % (i+1)
