def base(num, b):
    i = 0
    val = 0
    while num != 0:
        val += (num & 1) * (b ** i)
        i += 1
        num >>= 1
    return val


def is_prime(num, d):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            # print('\t', num, i)
            d.append(i)
            return False
    # print('\tprime:', num)
    return True


def check_ones(num):
    return num & (2 ** (n - 1)) and num & 1


for t in range(int(raw_input())):
    n, j = map(int, raw_input().strip().split())
    p = 2 ** (n - 1)
    print('Case #' + str(t + 1) + ':')
    while j != 0:
        if check_ones(p):
            # print('debug:', p, bin(p)[2:])
            divs = []
            for i in range(2, 11):
                # print('\t\tb=', i, end='')
                if is_prime(int(base(p, i)), divs):
                    break
            else:
                j -= 1
                print('{0} {1}'.format(bin(p)[2:], ' '.join(map(str, divs))))
        p += 1
