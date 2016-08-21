# Google Code Jam 2016
# Round 1B
# Problem A: Getting the Digits
# Author: Leonardy Kristianto (leonardy)

from collections import Counter

with open("A-large.in", "r") as f:
    cases = int(f.readline())

    for case in range(cases):
        line = str(f.readline())

        dict1 = Counter(list(line.strip()))

        dict2 = {}

        # for 0, 2, 4, 6, 8

        if dict1['Z'] != 0:
            dict2['0'] = 0  # initialize
            for i in range(dict1['Z']):
                dict2['0'] += 1
                dict1['Z'] -= 1
                dict1['E'] -= 1
                dict1['R'] -= 1
                dict1['O'] -= 1

        if dict1['W'] != 0:
            dict2['2'] = 0  # initialize
            for i in range(dict1['W']):
                dict2['2'] += 1
                dict1['T'] -= 1
                dict1['W'] -= 1
                dict1['O'] -= 1

        if dict1['U'] != 0:
            dict2['4'] = 0  # initialize
            for i in range(dict1['U']):
                dict2['4'] += 1
                dict1['F'] -= 1
                dict1['O'] -= 1
                dict1['U'] -= 1
                dict1['R'] -= 1

        if dict1['X'] != 0:
            dict2['6'] = 0  # initialize
            for i in range(dict1['X']):
                dict2['6'] += 1
                dict1['S'] -= 1
                dict1['I'] -= 1
                dict1['X'] -= 1

        if dict1['G'] != 0:
            dict2['8'] = 0  # initialize
            for i in range(dict1['G']):
                dict2['8'] += 1
                dict1['E'] -= 1
                dict1['I'] -= 1
                dict1['G'] -= 1
                dict1['H'] -= 1
                dict1['T'] -= 1

        # now for 1, 3, 5, 7

        if dict1['O'] != 0:
            dict2['1'] = 0  # initialize
            for i in range(dict1['O']):
                dict2['1'] += 1
                dict1['O'] -= 1
                dict1['N'] -= 1
                dict1['E'] -= 1

        if dict1['T'] != 0:
            dict2['3'] = 0  # initialize
            for i in range(dict1['T']):
                dict2['3'] += 1
                dict1['T'] -= 1
                dict1['H'] -= 1
                dict1['R'] -= 1
                dict1['E'] -= 2

        if dict1['F'] != 0:
            dict2['5'] = 0  # initialize
            for i in range(dict1['F']):
                dict2['5'] += 1
                dict1['F'] -= 1
                dict1['I'] -= 1
                dict1['V'] -= 1
                dict1['E'] -= 1

        if dict1['S'] != 0:
            dict2['7'] = 0  # initialize
            for i in range(dict1['S']):
                dict2['7'] += 1
                dict1['S'] -= 1
                dict1['E'] -= 2
                dict1['V'] -= 1
                dict1['N'] -= 1

        if dict1['I'] != 0:
            dict2['9'] = 0  # initialize
            for i in range(dict1['I']): # small bug here
                dict2['9'] += 1
                dict1['N'] -= 2
                dict1['I'] -= 1
                dict1['E'] -= 1

        # print dict1
        # print dict2

        num = ""

        for key in dict2:
            for char in range(0, dict2[key]):
                num += key

        print "Case #%i:" % (case + 1), ''.join(sorted(num))
