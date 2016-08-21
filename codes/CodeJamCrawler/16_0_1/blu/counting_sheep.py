#!/usr/bin/env python

def get_digits(n):
    digits = set()
    while n:
        digit = n % 10
        n //= 10
        digits.add(digit)
       
    return digits

def counting_sheep(n):
    digits = set()
    j = 0
    end = 0
    count_to_break = 0

    while len(digits) != 10:
        start = end
        j += 1
        digits = digits.union(get_digits(j*n))
        end = len(digits)

        if start == end:
            count_to_break += 1
        else:
            count_to_break = 0
        if count_to_break == 90:
            break
    else:
        return j*n
    return 'INSOMNIA'

nb = int(input())

for i in range(1, nb +1):
    n = input()
    last = counting_sheep(int(n))

    print('Case #{}: {}'.format(i,last))
