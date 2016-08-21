from redef_io import *


def get_digits(x=1):
    digits = []
    while x > 0:
        digits.append(x % 10)
        x /= 10
    return digits

t = int(raw_input())

for it in range(t):
    n = int(raw_input())

    digit_found = [False] * 10
    k = 1
    cont = True
	
    while not all(digit_found):
        if n * k == n * (k - 1):
            print_file('INSOMNIA')
            cont = False
            break

        for d in str(n * k):
            digit_found[int(d)] = True

        k += 1

    if cont:
        print_file(n * (k - 1))