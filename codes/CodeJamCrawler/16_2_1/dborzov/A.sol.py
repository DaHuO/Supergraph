#!/usr/bin/env python

# A.py

import sys


input_data = open(sys.argv[1])
filename = ".".join(sys.argv[1].split(".")[:-1])
output_data = open(filename + ".out","w")

def readline():
    return input_data.readline().rstrip()

letters = {
   0: "ZERO",
   1: "ONE",
   2: "TWO",
   3: "THREE",
   4:"FOUR",
   5: "FIVE",
   6: "SIX",
   7: "SEVEN",
   8: "EIGHT",
   9: "NINE"
}

clear_order = [
    ('Z', 0),
    ('G', 8),
    ('U', 4),
    ('R', 3),
    ('F', 5),
    ('V', 7),
    ('W', 2),
    ('X', 6),
    ('O', 1),
    ('I', 9)
]

l_ps = {}
for digit, spelled in letters.iteritems():
    cur = {}
    for letter in spelled:
        cur[letter] = cur.get(letter,0) + 1
    l_ps[digit] = cur

# import pdb; pdb.set_trace()



def how_many_keys(count, key_letter):
    return count[key_letter]

num_tests = int(readline())
for i in range(1,num_tests+1):
    line = readline()
    counts = {}
    for letter in line:
        counts[letter] = counts.get(letter,0) + 1

    def substract(count, minus, repeats):
        for letter, num in minus.iteritems():
            count[letter] = count[letter] - repeats*minus[letter]

    result = []
    for key, digit in clear_order:
        if counts.get(key,0)==0:
            continue
        number_of_occ = counts[key]
        # print '%s letters for %s in %s ' % (number_of_occ, digit, line)
        substract(counts, l_ps[digit], number_of_occ)
        result = result + [digit for _ in range(number_of_occ)]
    result = sorted(result)
    output_data.write("Case #%s: %s\n" % (i, "".join([str(d) for d in result])))