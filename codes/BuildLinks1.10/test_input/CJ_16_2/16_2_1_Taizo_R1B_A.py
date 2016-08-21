
# -*- coding: utf8 -*-

import sys

# inputFile = "A-small-attempt0.in"
# inputFile = "A-large-practice.in"
inputFile = "A-large.in"
f = open(inputFile)
sys.stdout = open(inputFile.replace(".in", ".txt"), 'w')
tc_num = int(f.readline().rstrip())

k1 = {"Z": ["ZERO", 0], "W": ["TWO", 2], "U": ["FOUR", 4], "X": ["SIX", 6], "G": ["EIGHT", 8]}
k2 = {"O": ["ONE", 1], "R": ["THREE", 3], "F": ["FIVE", 5], "S": ["SEVEN", 7]}
k3 = {"I": ["NINE", 9]}

for tc in range(tc_num):
    s = f.readline().rstrip()

    numbers = []
    for k in k1:
        # sys.stderr.write(k + "\n")
        while k in s:
            # sys.stderr.write(s + "\n")
            for c in k1[k][0]:
                s = s.replace(c, "", 1)
            numbers.append(k1[k][1])

    for k in k2:
        while k in s:
            for c in k2[k][0]:
                s = s.replace(c, "", 1)
            numbers.append(k2[k][1])

    for k in k3:
        while k in s:
            for c in k3[k][0]:
                s = s.replace(c, "", 1)
            numbers.append(k3[k][1])

    numbers.sort()

    ans = ""
    for n in numbers:
        ans += str(n)

    print("Case #" + str(tc + 1) + ": " + ans)

