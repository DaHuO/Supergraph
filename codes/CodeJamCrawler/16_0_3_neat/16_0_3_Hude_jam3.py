# def sol_print(value):
#     sol_print.line_number += 1;
#     print "Case #%d: %s"%(sol_print.line_number, value)

# sol_print.line_number = 0

import random

def newton_sqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def get_value_base(str, base):
    n = 0
    str = str[::-1]
    for i, atomic in enumerate(str):
        n += (base ** i) * int(atomic)
    return n

def get_divisor(n):
    if n % 2 == 0:
        return 2;
    else:
        sqrt = newton_sqrt(n)
        for i in range(3, sqrt, 2):
            if n % i == 0:
                return i
    return -1

def generate_random_series(size):
    first_last = "1"
    middle = ""
    for i in range(size - 2):
        middle += (random.randint(0, 1)).__str__()
    return first_last + middle + first_last


T = int(raw_input())
for i in range(T):
    inputs = map(int, raw_input().split())
N = inputs[0]
J = inputs[1]

count = 0
results = []
while count < J:
    str = generate_random_series(N)
    divisors = []
    for i in range(2, 11):
        nb = get_value_base(str,i)
        divisor = get_divisor(nb)
        if divisor == -1:
            break;
        divisors.append(divisor)
    else:
        if len(results) != 0:
            strs, null = zip(*results)
        else:
            strs = []
        if str not in strs:
            results.append((str, divisors))
            count += 1

print "Case #1:"
for str, divisors in results:
    divisors_str = " "
    for divisor in divisors:
        divisors_str += divisor.__str__() + " "
    print str + divisors_str