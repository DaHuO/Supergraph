# coding=utf-8

import sys


def find_n(N, storage, retrys):
    number = retrys * N
    copy = number

    if number == 0 or retrys == 10000:
        return "INSOMNIA"

    while number > 0:
        remains = number % 10
        try:
            index = storage.index(remains)
            del storage[index]
        except:
            pass

        number = int(number / 10)

    if len(storage) == 0:
        return copy
    else:
        retrys += 1

        return find_n(N, storage, retrys)


def main():
    T = int(raw_input())

    for i in range(0, T, 1):
        storage = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        N = int(raw_input())

        print "Case #{}: {}".format(i + 1, find_n(N, storage, 1))


if __name__ == '__main__':
    sys.exit(main())
