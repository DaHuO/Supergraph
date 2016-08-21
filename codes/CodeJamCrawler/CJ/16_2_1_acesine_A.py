T = int(raw_input())

for t in range(1, T+1):
    s = raw_input().rstrip();
    d = []
    m = {}
    for x in s:
        if x in m.keys():
            m[x] += 1
        else:
            m[x] = 1
    # ZERO
    if 'Z' in m.keys() and m['Z'] != 0:
        x = m['Z']
        d.extend([0]*x)
        m['Z'] -= x
        m['E'] -= x
        m['R'] -= x
        m['O'] -= x
    # TWO
    if 'W' in m.keys() and m['W'] != 0:
        x = m['W']
        d.extend([2]*x)
        m['T'] -= x
        m['W'] -= x
        m['O'] -= x
    # FOUR
    if 'U' in m.keys() and m['U'] != 0:
        x = m['U']
        d.extend([4]*x)
        m['F'] -= x
        m['O'] -= x
        m['U'] -= x
        m['R'] -= x
    # THREE
    if 'R' in m.keys() and m['R'] != 0:
        x = m['R']
        d.extend([3]*x)
        m['T'] -= x
        m['H'] -= x
        m['R'] -= x
        m['E'] -= 2*x
    # EIGHT
    if 'H' in m.keys() and m['H'] != 0:
        x = m['H']
        d.extend([8]*x)
        m['E'] -= x
        m['I'] -= x
        m['G'] -= x
        m['H'] -= x
        m['T'] -= x
    # ONE
    if 'O' in m.keys() and m['O'] != 0:
        x = m['O']
        d.extend([1]*x)
        m['O'] -= x
        m['N'] -= x
        m['E'] -= x
    # FIVE
    if 'F' in m.keys() and m['F'] != 0:
        x = m['F']
        d.extend([5]*x)
        m['F'] -= x
        m['I'] -= x
        m['V'] -= x
        m['E'] -= x
    # SIX
    if 'X' in m.keys() and m['X'] != 0:
        x = m['X']
        d.extend([6]*x)
        m['S'] -= x
        m['I'] -= x
        m['X'] -= x
    # SEVEN
    if 'S' in m.keys() and m['S'] != 0:
        x = m['S']
        d.extend([7]*x)
        m['S'] -= x
        m['E'] -= 2*x
        m['V'] -= x
        m['N'] -= x
    # NINE
    if 'E' in m.keys() and m['E'] != 0:
        x = m['E']
        d.extend([9]*x)
        m['N'] -= 2*x
        m['I'] -= x
        m['E'] -= x
    d.sort()
    print("Case #%d: %s" % (t, "".join([str(x) for x in d])))
