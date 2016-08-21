import fileinput, sys

def slurp(s):
    d = {}
    for c in s:
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1
    return d

def solve(s):
    d = slurp(s.rstrip())
    a = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    if 'Z' in d and d['Z'] > 0:
        a[0] = d['Z']
        d['Z'] = 0
        d['E'] = d['E'] - a[0]
        d['R'] = d['R'] - a[0]
        d['O'] = d['O'] - a[0]

    if 'W' in d and d['W'] > 0:
        a[2] = d['W']
        d['W'] = 0
        d['T'] = d['T'] - a[2]
        d['O'] = d['O'] - a[2]

    if 'X' in d and d['X'] > 0:
        a[6] = d['X']
        d['X'] = 0
        d['S'] = d['S'] - a[6]
        d['I'] = d['I'] - a[6]

    if 'G' in d and d['G'] > 0:
        a[8] = d['G']
        d['G'] = 0
        d['E'] = d['E'] - a[8]
        d['I'] = d['I'] - a[8]
        d['H'] = d['H'] - a[8]
        d['T'] = d['T'] - a[8]

    if 'T' in d and d['T'] > 0:
        a[3] = d['T']
        d['T'] = 0
        d['H'] = d['H'] - a[3]
        d['R'] = d['R'] - a[3]
        d['E'] = d['E'] - a[3] - a[3]

    if 'R' in d and d['R'] > 0:
        a[4] = d['R']
        d['R'] = 0
        d['F'] = d['F'] - a[4]
        d['O'] = d['O'] - a[4]
        d['U'] = d['U'] - a[4]

    if 'O' in d and d['O'] > 0:
        a[1] = d['O']
        d['O'] = 0
        d['N'] = d['N'] - a[1]
        d['E'] = d['E'] - a[1]

    if 'F' in d and d['F'] > 0:
        a[5] = d['F']
        d['F'] = 0
        d['I'] = d['I'] - a[5]
        d['V'] = d['V'] - a[5]
        d['E'] = d['E'] - a[5]

    if 'V' in d and d['V'] > 0:
        a[7] = d['V']
        d['V'] = 0
        d['S'] = d['S'] - a[7]
        d['E'] = d['E'] - a[7] - a[7]
        d['N'] = d['N'] - a[7]

    if 'I' in d and d['I'] > 0:
        a[9] = d['I']
        d['I'] = 0
        d['E'] = d['E'] - a[9]
        d['N'] = d['N'] - a[9] - a[9]

    for n in d.keys():
        assert(d[n] == 0)

    x = ""
    for i in range(0, 10):
        for j in range(0, a[i]):
            x = x + str(i)

    return x

index = 0
for line in fileinput.input():
    index += 1
    if index == 1:
        continue
    print("Case #%d: %s" % (index - 1, solve(line)))
