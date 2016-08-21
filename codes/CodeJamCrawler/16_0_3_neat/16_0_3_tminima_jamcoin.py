import math


def prime(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False, i
    return True, 0


def get_strings(n, l):
    for i in range(2**n):
        num = format(i, "0{}b".format(n - 2))
        yield bytearray("{}{}{}".format(1, num, 1), encoding="utf-8")


def get_jamcoin(n, j):
    print("Case #1:")
    bin_strings = get_strings(n, j)

    while j:
        flag = 1
        factors = []
        number = next(bin_strings)
        for base in range(2, 11):
            base_num = int(number, base)
            # print(base_num)
            is_prime, factor = prime(base_num)
            if is_prime:
                flag = 0
                break
            factors.append(str(factor))
        if flag:
            j -= 1
            print(number.decode("utf8"), " ".join(factors))


if __name__ == "__main__":
    data = open("input.txt", "r").readlines()
    data = [i.strip() for i in data]
    n = int(data[1].split()[0])
    j = int(data[1].split()[1])

    get_jamcoin(n, j)
