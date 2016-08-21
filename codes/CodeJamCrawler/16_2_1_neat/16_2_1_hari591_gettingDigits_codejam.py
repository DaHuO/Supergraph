t = input()
j = 0
while t:
    t -= 1
    j += 1
    d = {}
    numbers = {}
    s = raw_input().strip()
    for each in s:
        if d.has_key(each):
            d[each] += 1
        else:
            d[each] = 1
    if d.has_key('Z'):
        numbers[0] = d['Z']
        d['E'] -= d['Z']
        d['R'] -= d['Z']
        d['O'] -= d['Z']
    if d.has_key('W'):
        numbers[2] = d['W']
        d['T'] -= d['W']
        d['O'] -= d['W']

    if d.has_key('U'):
        numbers[4] = d['U']
        d['F'] -= d['U']
        d['O'] -= d['U']
        d['R'] -= d['U']

    if d.has_key('X'):
        numbers[6] = d['X']
        d['S'] -= d['X']
        d['I'] -= d['X']

    if d.has_key('G'):
        numbers[8] = d['G']
        d['E'] -= d['G']
        d['I'] -= d['G']
        d['H'] -= d['G']
        d['T'] -= d['G']

    if d.has_key('R') and d['R'] != 0:
        numbers[3] = d['R']

    if d.has_key('F') and d['F'] != 0:
        numbers[5] = d['F']
        d['V'] -= d['F']

    if d.has_key('V') and d['V'] != 0:
        numbers[7] = d['V']
        d['N'] -= d['V']

    if d.has_key('O') and d['O'] != 0:
        numbers[1] = d['O']
        d['N'] -= d['O']

    if d.has_key('N') and d['N'] != 0:
        numbers[9] = d['N'] /2

    s = ""
    for i in range(10):
        if numbers.has_key(i):
            s += str(i) * numbers[i]
    print "Case #" + str(j) +  ": " + s




