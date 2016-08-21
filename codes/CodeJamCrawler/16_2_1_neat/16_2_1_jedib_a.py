#!/usr/bin/python

tests = int(raw_input())

for test in xrange(1, tests+1):
    chaine = raw_input()
    dico = {}
    dico1 = {}
    dico['A'] = 0
    dico['B'] = 0
    dico['C'] = 0
    dico['D'] = 0
    dico['E'] = 0
    dico['F'] = 0
    dico['G'] = 0
    dico['H'] = 0
    dico['I'] = 0
    dico['J'] = 0
    dico['K'] = 0
    dico['L'] = 0
    dico['M'] = 0
    dico['N'] = 0
    dico['O'] = 0
    dico['P'] = 0
    dico['Q'] = 0
    dico['R'] = 0
    dico['S'] = 0
    dico['T'] = 0
    dico['U'] = 0
    dico['V'] = 0
    dico['W'] = 0
    dico['X'] = 0
    dico['Y'] = 0
    dico['Z'] = 0
    for letter in chaine:
        dico[letter] += 1 

    if dico['Z']:
        val = dico['Z']
        dico1[0] = val
        dico['E'] -= val
        dico['R'] -= val
        dico['O'] -= val
    if dico['W']:
        val = dico['W']
        dico1[2] = val
        dico['T'] -= val
        dico['O'] -= val
    if dico['U']:
        val = dico['U']
        dico1[4] = val
        dico['F'] -= val
        dico['O'] -= val
        dico['R'] -= val
    if dico['X']:
        val = dico['X']
        dico1[6] = val
        dico['S'] -= val
        dico['I'] -= val
    if dico['G']:
        val = dico['G']
        dico1[8] = val
        dico['E'] -= val
        dico['I'] -= val
        dico['H'] -= val
        dico['T'] -= val
    if dico['F']:
        val = dico['F']
        dico1[5] = val
        dico['I'] -= val
        dico['V'] -= val
        dico['E'] -= val
    if dico['T']:
        val = dico['T']
        dico1[3] = val
        dico['H'] -= val
        dico['R'] -= val
        dico['E'] -= (2*val)
    if dico['S']:
        val = dico['S']
        dico1[7] = val
        dico['E'] -= (2*val)
        dico['V'] -= val
        dico['N'] -= val
    if dico['O']:
        val = dico['O']
        dico1[1] = val
        dico['N'] -= val
        dico['E'] -= val
    if dico['I']:
        val = dico['I']
        dico1[9] = val

    res = ""
    for key, value in sorted(dico1.iteritems()):
        res += (value * str(key))

    print "Case #%i: %s" % (test, res) 

