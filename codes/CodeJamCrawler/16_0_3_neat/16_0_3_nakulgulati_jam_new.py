from math import sqrt
from random import *


def is_prime(a):
    up = int(sqrt(a))
    for i in range(2, up + 1):
        if a % i == 0:
            return i
    return True


def check_num(num_in):
    div_list = []
    for b in range(2, 11):
        num_b = int(num_in, base=b)
        val = is_prime(num_b)
        div_list.append(val)

    if True not in div_list:
        divs = " ".join(str(x) for x in div_list)
        print("{} {}".format(num_in, divs))
        return True

    return False


randBinList = lambda p: [randint(0, 1) for b in range(1, p + 1)]

t = int(input())
for i in range(1, t + 1):
    n, j = [int(s) for s in input().split(" ")]

    visted = []

    print("Case #{}:".format(i))
    count = 0
    while count != j:
        rand_list = randBinList(n - 2)
        rand = "".join(str(x) for x in rand_list)
        num = "1" + rand + "1"
        if num in visted:
            continue

        visted.append(num)
        val = check_num(num)
        if val:
            count += 1
