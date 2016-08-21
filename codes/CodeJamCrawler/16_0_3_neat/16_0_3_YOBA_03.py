import math
import itertools
import random

import tqdm


def get_divisor(x):

    if x % 2 == 0:

        return 2

    for divisor in range(3, math.ceil(math.sqrt(x)), 2):

        if x % divisor == 0:

            return divisor

        if divisor > 300:

            break


def generate(count):

    viewed = set()
    while True:

        x = random.randint(0, (1 << count) - 1)
        if x not in viewed:

            viewed.add(x)
            yield str.format("{value:0>{digits}b}", digits=count, value=x)


n, j = map(int, str.split(input()))
count = 0
print("Case #1:")
for ci in range(2 ** (n - 2)):

    s = "1" + str.format("{value:0>{digits}b}", digits=n - 2, value=ci) + "1"
    divisors = []
    for base in range(2, 11):

        i = int(s, base)
        divisor = get_divisor(i)
        if divisor is None:

            break

        divisors.append(divisor)

    if len(divisors) == 9:

        print(s, *map(str, divisors))
        count += 1

    if count == j:

        break
