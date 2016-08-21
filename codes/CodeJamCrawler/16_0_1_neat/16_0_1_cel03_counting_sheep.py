num_cases = int(raw_input())

for num_case in list(xrange(1, num_cases + 1)):

    first_num = int(raw_input())
    digits_seen = list()

    if first_num == 0:
        print 'Case #{}: {}'.format(num_case, 'INSOMNIA')
    else:
        n = 1
        while True:
            for digit in str(first_num*n):
                try:
                    digits_seen.index(digit)
                except ValueError, e:
                    digits_seen.append(digit)

            if digits_seen.__len__() == 10:
                print 'Case #{}: {}'.format(num_case, first_num*n)
                break
            n = n + 1
