import sys
from itertools import *
from operator import itemgetter
def read_int():
    k = sys.stdin.readline().strip()
    return int(k)

def read_line():
    return sys.stdin.readline().strip()


def unique_justseen(iterable, key=None):
    "List unique elements, preserving order. Remember only the element just seen."
    # unique_justseen('AAAABBBCCDAABBB') --> A B C D A B
    # unique_justseen('ABBCcAD', str.lower) --> A B C A D
    return imap(next, imap(itemgetter(1), groupby(iterable, key)))

def dedups(s):
    return "".join(unique_justseen(s))

def main():
    c = read_int()
    for i in range(c):
        s = dedups(read_line())
        l = len(s)
        res = l - 1 if s[-1] == '+' else l
        print "Case #%d: %s" % (i+1, res)


if __name__ == "__main__":
    main()
