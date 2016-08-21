#!/usr/bin/python3.4

import sys
import math
from functools import reduce

def solve(s):
    #words = ["ONE", "THREE", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    #ht = {}
    #for w in words:
    #    for c in w:
    #        ht[c] = ht.get(c, 0)  +1 

    #print(ht)
    #print(s)
    ht_s = {}
    for c in s:
        ht_s[c] = ht_s.get(c, 0) + 1

    s = ''

    nb = ht_s.get('Z', 0)
    s += '0' * nb
    extract(ht_s, 'ZERO', nb)

    nb_two = ht_s.get('W', 0)
    extract(ht_s, 'TWO', nb_two)

    nb_four = ht_s.get('U', 0)
    extract(ht_s, 'FOUR', nb_four)

    nb = ht_s.get('O', 0)
    extract(ht_s, 'ONE', nb)
    s += '1' * nb

    s += '2' * nb_two

    nb_height = ht_s.get('G', 0)
    extract(ht_s, 'EIGHT', nb_height)

    nb = ht_s.get('T', 0)
    s += '3' * nb
    extract(ht_s, 'THREE', nb)

    s += '4' * nb_four

    nb = ht_s.get('F', 0)
    s += '5' * nb
    extract(ht_s, 'FIVE', nb)

    nb = ht_s.get('X', 0)
    s += '6' * nb
    extract(ht_s, 'SIX', nb)

    nb = ht_s.get('S', 0)
    s += '7' * nb
    extract(ht_s, 'SEVEN', nb)

    s += '8' * nb_height

    nb = ht_s.get('I', 0)
    s += '9' * nb
    extract(ht_s, 'NINE', nb)

    return s

def extract(ht, s, n):
    if n == 0:
        return
    for c in s:
        ht[c] -= n

def main():
    nb = int(get_line())
    for case_id in range(1, nb + 1):
        s = get_line()

        ret = solve(s)
        print('Case #%d: %s' %(case_id, ret), file = o)

def get_line():
    return f.readline().strip()

def open_files():
    if len(sys.argv) == 1:
        f = sys.stdin
        o = sys.stdout

    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'r')
        o = sys.stdout

    if len(sys.argv) == 3:
        f = open(sys.argv[1], 'r')
        o = open(sys.argv[2], 'w')

    return (f, o)

if __name__ == "__main__":
    (f, o) = open_files()
    main()

