import sys
import random


def examine(number, a_list):
    number = str(number)
    for digit in number:
        if digit not in a_list:
            a_list.append(digit)


if __name__ == "__main__":
    sys.stdin = open("A-large.in")
    sys.stdout = open("small.txt", "w")
    for case in range(1, int(sys.stdin.readline())+1):
        n = int(sys.stdin.readline())
        seen_digits = []
        if n == 0:
            result = "INSOMNIA"
        else:
            i = 1
            while len(seen_digits) != 10:
                examine(n*i, seen_digits)
                i += 1
                #print seen_digits
            result = str(n*(i-1))
        print "Case #%d: %s" % (case, result)

