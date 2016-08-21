from math import sqrt
from random import randint


def get_divisor(n):
    for i in range(2, round(sqrt(n))+1):
        if n % i == 0:
            return i
    return None

counter = 0
print("Case #1:")
while counter < 50:
    l = [1]
    for i in range(14):
        l.append(randint(0, 1))
    l.append(1)
    divisors = []
    for base in range(2, 11):
        num = 0
        mul = 1
        for i in range(15, -1, -1):
            num += l[i]*mul
            mul *= base
        if get_divisor(num) is None:
            divisors = []
            break
        else:
            divisors.append(str(get_divisor(num)))
    if len(divisors)>0:
        print("".join((str(x) for x in l)), " ".join(divisors))
        counter += 1
