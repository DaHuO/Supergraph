#!/usr/bin/python

t = int(raw_input())

for i in range(t):
    string = raw_input()
    letters = {}
    digits = []
    for c in string:
        try:
            letters[c] += 1
        except KeyError:
            letters[c] = 1
    while 'Z' in letters and letters['Z'] > 0:
        letters['Z'] -= 1
        letters['E'] -= 1
        letters['R'] -= 1
        letters['O'] -= 1
        digits.append(0)
    while 'W' in letters and letters['W'] > 0:
        letters['T'] -= 1
        letters['W'] -= 1
        letters['O'] -= 1
        digits.append(2)
    while 'X' in letters and letters['X'] > 0:
        letters['S'] -= 1
        letters['I'] -= 1
        letters['X'] -= 1
        digits.append(6)
    while 'G' in letters and letters['G'] > 0:
        letters['E'] -= 1
        letters['I'] -= 1
        letters['G'] -= 1
        letters['H'] -= 1
        letters['T'] -= 1
        digits.append(8)
    while 'U' in letters and letters['U'] > 0:
        letters['F'] -= 1
        letters['O'] -= 1
        letters['U'] -= 1
        letters['R'] -= 1
        digits.append(4)
    while 'F' in letters and letters['F'] > 0:
        letters['F'] -= 1
        letters['I'] -= 1
        letters['V'] -= 1
        letters['E'] -= 1
        digits.append(5)
    while 'T' in letters and letters['T'] > 0:
        letters['T'] -= 1
        letters['H'] -= 1
        letters['R'] -= 1
        letters['E'] -= 1
        letters['E'] -= 1
        digits.append(3)
    while 'O' in letters and letters['O'] > 0:
        letters['O'] -= 1
        letters['N'] -= 1
        letters['E'] -= 1
        digits.append(1)
    while 'S' in letters and letters['S'] > 0:
        letters['S'] -= 1
        letters['E'] -= 1
        letters['V'] -= 1
        letters['E'] -= 1
        letters['N'] -= 1
        digits.append(7)
    while 'N' in letters and letters['N'] > 0:
        letters['N'] -= 1
        letters['I'] -= 1
        letters['N'] -= 1
        letters['E'] -= 1
        digits.append(9)
    print 'Case #{0}: {1}'.format(i+1, ''.join(map(str, sorted(digits))))
