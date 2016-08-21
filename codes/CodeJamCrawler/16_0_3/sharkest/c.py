from itertools import product
import math


first_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
def first_divisor(n):
    for x in first_primes:
        if n % x == 0:
            return x
            break

    return n

n = 32
j = 500
found = 0

print("Case #1:")

ans = []

for string in map(''.join, product('10', repeat=n - 2)):
    string = "1" + string + "1"
    divisors = []
    valid = True
    for i in range(2, 11):
        number = int(string, i)
        divisor = first_divisor(number)
        if(divisor == number):
            valid = False
            break
        divisors.append(divisor)
    if valid is False:
        continue
    if len(divisors) == 9:
        ans.append([string, divisors])
        # print(len(ans))
    if len(ans) == j:
        break

for string, divisors in ans:
    divisors_string = ''.join(str(e) + ' ' for e in divisors)
    divisors_string = divisors_string[:-1]
    ans_string = string + ' ' + divisors_string
    print(ans_string)
