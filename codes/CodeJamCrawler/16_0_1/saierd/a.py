#!/usr/bin/env python3

import sys


def last_number(n):
    if n == 0:
        return "INSOMNIA"

    x = n
    digits = set()

    while True:
        digits.update(str(x))

        if len(digits) == 10:
            return x

        x += n


def main():
    output = []

    with open(sys.argv[1]) as f:
        data = f.readlines()

    for i, n_str in enumerate(data[1:]):
        n = int(n_str)
        y = last_number(n)
        output.append("Case #{}: {}".format(i + 1, y))

    with open("output.txt", "w") as f:
        f.write("\n".join(output))


if __name__ == "__main__":
    main()
