"""
Google qualification round, Coin Jam

@author: Faegheh Hasibi
"""
import math


def coin_jam(n, j):
    """Computes jamcoins

    :param n: length of jamcoin
    :param j: number of distinct jamcoins of length n
    :return: {jamcoin:[d1, ..], ...}
    """
    num = "1" + (n-2) * "0" + "1"
    i = 0
    jamcoins = {}
    while i < j:
        if is_jamcoin(num):
            jamcoins[num] = get_divisors(num)
            i += 1
            print(str(num) + " " + " ".join(str(div) for div in jamcoins[num]))
        num = bin(int(num, 2) + 2)[2:]
    return jamcoins


def get_divisors(num):
    """ Gets the first non-trivial divisors for bases [2..10]

    :param num: binary number in string, e.g. '101'
    :return: list of divisors
    """
    divisors = []
    for i in range(2, 11):
        num_n = int(num, i)
        for j in range(2, num_n):
            if num_n % j == 0:
                divisors.append(j)
                break
    return divisors


def is_jamcoin(num):
    """For all bases in range [2..10], the resulting number should not be prime"""
    return all([not is_prime(int(num, n)) for n in range(10, 1, -1)])


def is_prime(num):
    return all(num % i for i in range(2, int(math.sqrt(num)) + 2))


def out_format(jamcoins):
    """converts jamcoins dictionary to output format"""
    out_str = ""
    for jc in sorted(jamcoins):
        out_str += str(jc) + " " + " ".join(str(div) for div in jamcoins[jc]) + "\n"
    return out_str


def main():
    print("Case #1:")
    coin_jam(16, 50)

if __name__ == "__main__":
    main()