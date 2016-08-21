#!/usr/bin/python


def main():
    with open("input.txt") as f:
        inputs = [line.strip() for line in f]
        del inputs[0]
        for i, x in enumerate(inputs):
            z = "+" * len(x)
            count = 0
            cur = x[:]
            while cur != z:
                cur = flip(cur, find_farthest_right(cur))
                count += 1
            print("Case #{}: {}".format(i+1, count))


def find_farthest_right(inp):
    return inp.rfind("-")


def flip(inp, loc):
    for x in range(loc+1):
        if inp[x] == "-":
            inp = inp[:x] + "+" + inp[x+1:]
        else:
            inp = inp[:x] + "-" + inp[x+1:]
    return inp


main()
