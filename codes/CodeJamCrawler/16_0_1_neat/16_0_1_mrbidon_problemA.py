# -*- coding: utf8

import sys

def get_nb(nb, s):
    #print "{0} {1}".format(nb, s)
    while nb != 0 :
        s.add(nb % 10)
        nb = nb /10



def count_sheep(nb):
    s = set()
    i = 1
    test_nb = nb
    while set([0,1,2,3,4,5,6,7,8,9]) != s :
        test_nb = nb*i
        get_nb(test_nb, s)
        i += 1


    return test_nb

def main(nbs):
    i = 1
    for nb in nbs :
        if nb == 0:
            print "Case #{0}: INSOMNIA".format(i)
        else:
            print "Case #{0}: {1}".format(i, count_sheep(nb))
        i += 1
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    input = []
    for line in sys.stdin :
        input.append(int(line))

    main(input)
