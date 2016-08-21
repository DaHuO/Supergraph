import math

non_trivial_divisors = dict()


def get_non_trivial_divisor(num):
    if num in non_trivial_divisors:
        return non_trivial_divisors[num]
    sqrt_num = round(math.sqrt(num))
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            non_trivial_divisors[num] = i
            return i


def generator(N, J):
    count = 0
    smallest = int('1' + (N - 2) * '0' + '1', 2)
    largest = int(N * '1', 2)
    print('Case #1:')
    for i in range(smallest, largest + 1):
        i = bin(i)[2:]
        if i[0] != '1' or i[-1] != '1':
            continue
        divisors = []
        for base in range(2, 11):
            num = int(i, base)
            divisor = get_non_trivial_divisor(num)
            if divisor:
                divisors.append(str(divisor))
            else:
                break
        else:
            print('{} {}'.format(i, ' '.join(divisors)))
            count += 1
        if count == J:
            break


generator(16, 50)
# generator(32, 500)
