#!/usr/bin/env python3

def main(i):
    digits = set()
    starting_num = num = int(input())

    if not starting_num:
        return "Case #{}: {}".format(i, "INSOMNIA")

    while len(digits) < 10:
        curr_digits = list(str(num))

        for digit in curr_digits:
            digits.add(digit)

        num += starting_num

    return "Case #{}: {}".format(i, num - starting_num)

if __name__ == '__main__':
    tests = int(input())

    for i in range(tests):
        print(main(i + 1))
