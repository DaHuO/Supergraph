import collections

N = int(input())

for j in range(N):
    print("Case #" + str(j + 1) + ": ", end="")

    s = input()
    m = collections.defaultdict(int)

    num = []

    for c in s:
        m[c] += 1

    # ZERO
    for i in range(m['Z']):
        num.append(0)
    m['E'] -= m['Z']
    m['R'] -= m['Z']
    m['O'] -= m['Z']
    m['Z'] = 0

    # TWO
    for i in range(m['W']):
        num.append(2)
    m['T'] -= m['W']
    m['O'] -= m['W']
    m['W'] = 0

    # FOUR
    for i in range(m['U']):
        num.append(4)
    m['F'] -= m['U']
    m['O'] -= m['U']
    m['R'] -= m['U']
    m['U'] = 0

    # SIX
    for i in range(m['X']):
        num.append(6)
    m['S'] -= m['X']
    m['I'] -= m['X']
    m['X'] = 0

    # EIGHT
    for i in range(m['G']):
        num.append(8)
    m['E'] -= m['G']
    m['I'] -= m['G']
    m['H'] -= m['G']
    m['T'] -= m['G']
    m['G'] = 0

    # THREE
    for i in range(m['R']):
        num.append(3)
    m['T'] -= m['R']
    m['H'] -= m['R']
    m['E'] -= m['R']
    m['E'] -= m['R']
    m['R'] = 0

    # FIVE
    for i in range(m['F']):
        num.append(5)
    m['I'] -= m['F']
    m['V'] -= m['F']
    m['E'] -= m['F']
    m['F'] = 0

    # SEVEN
    for i in range(m['V']):
        num.append(7)
    m['S'] -= m['V']
    m['E'] -= m['V']
    m['E'] -= m['V']
    m['N'] -= m['V']
    m['V'] = 0

    # ONE
    for i in range(m['O']):
        num.append(1)

    # NINE
    for i in range(m['I']):
        num.append(9)

    print("".join([str(k) for k in sorted(num)]))
