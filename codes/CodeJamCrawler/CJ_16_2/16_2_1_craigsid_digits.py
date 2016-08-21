
import sys
import string
import re

fname = sys.argv[1]

with open(fname) as f:
    # T - number of test cases
    T = int(string.split(f.readline())[0])
    #print "T {}".format(T)

    for t in range(T):
        # S - String
        S = string.split(f.readline())[0]
        #print "S {}".format(S)

        # count number of letters
        stats = {}
        for c in S:
            if c in stats:
                stats[c] += 1
            else:
                stats[c] = 1

        # get digits
        digits = []

        # ZERO
        while 'Z' in stats and stats['Z'] > 0:
            digits.append(0)
            stats['Z'] -= 1
            stats['E'] -= 1
            stats['R'] -= 1
            stats['O'] -= 1
        # TWO
        while 'W' in stats and stats['W'] > 0:
            digits.append(2)
            stats['T'] -= 1
            stats['W'] -= 1
            stats['O'] -= 1
        # SIX
        while 'X' in stats and stats['X'] > 0:
            digits.append(6)
            stats['S'] -= 1
            stats['I'] -= 1
            stats['X'] -= 1
        # FOUR
        while 'U' in stats and stats['U'] > 0:
            digits.append(4)
            stats['F'] -= 1
            stats['O'] -= 1
            stats['U'] -= 1
            stats['R'] -= 1
        # EIGHT
        while 'G' in stats and stats['G'] > 0:
            digits.append(8)
            stats['E'] -= 1
            stats['I'] -= 1
            stats['G'] -= 1
            stats['H'] -= 1
            stats['T'] -= 1
        # FIVE
        while 'F' in stats and stats['F'] > 0:
            digits.append(5)
            stats['F'] -= 1
            stats['I'] -= 1
            stats['V'] -= 1
            stats['E'] -= 1
        # ONE
        while 'O' in stats and stats['O'] > 0:
            digits.append(1)
            stats['O'] -= 1
            stats['N'] -= 1
            stats['E'] -= 1
        # THREE
        while 'T' in stats and stats['T'] > 0:
            digits.append(3)
            stats['T'] -= 1
            stats['H'] -= 1
            stats['R'] -= 1
            stats['E'] -= 2
        # SEVEN
        while 'S' in stats and stats['S'] > 0:
            digits.append(7)
            stats['S'] -= 1
            stats['E'] -= 2
            stats['V'] -= 1
            stats['N'] -= 1
        # NINE
        while 'N' in stats and stats['N'] > 0:
            digits.append(9)
            stats['N'] -= 2
            stats['I'] -= 1
            stats['E'] -= 1

        digits.sort()
        ds = re.sub(r'[\',\[\] ]', '', str(digits))
        print "Case #{}: {}".format(t+1, ds)

