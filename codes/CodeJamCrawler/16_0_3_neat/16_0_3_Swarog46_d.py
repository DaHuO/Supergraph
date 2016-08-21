import sys
import random


cache = [[base ** x for x in range(32)] for base in range(11)]

def get_based_num(new_num, base):
    res = 0
    i = 0

    while new_num > 0:
        tmp = int(new_num % 2)
        if tmp == 1:
            res += cache[base][i]

        new_num //= 2
        i += 1
    return res

def randbin2(d):
    mx = (2 ** d) - 1
    b = bin(random.randint(0, mx))
    s = b[2:].rjust(d, '1')
    s = s[:-1] +'1'
    return s

def find_div(n):
    for m in range(2, 1000):
        if not n % m:
            return m
    return False

tests_numbers = input().strip()
n, j = (int(s) for s in input().strip().split())

num = 0
iters = 0

print("Case #1:")

numbers = []
prime_numbers = []

while(iters < j):
    bin_num = randbin2(n)
    if bin_num in numbers or bin_num in prime_numbers:
        continue

    divisors = []
    for i in range(2, 11):
        num = int(get_based_num(int(bin_num, 2), i))

        div = find_div(num)
        if not div:
            prime_numbers.append(bin_num)
            num = 0
            break
        else:
            divisors.append(div)

    if num:
        numbers.append(bin_num)
        iters += 1
        print(str(bin_num) + " " + " ".join(map(lambda x: str(x), divisors)))

    divisors = []
