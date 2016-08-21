from itertools import count


def count_sheep(n):
    if n is 0:
        return "INSOMNIA"

    digits_left = {
        '0': True, '1': True, '2': True, '3': True, '4': True,
        '5': True, '6': True, '7': True, '8': True, '9': True
    }

    for factor in count(start=1):
        product = n * factor
        for d in str(product):
            digits_left.pop(d, None)
            if len(digits_left) <= 0:
                return str(product)

for i in range(1, int(input()) + 1):
    number = int(input())
    print("Case #" + str(i) + ": " + count_sheep(number))

