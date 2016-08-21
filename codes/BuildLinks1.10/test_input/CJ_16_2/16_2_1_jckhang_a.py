from collections import Counter
dic = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR',
       'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
t = int(raw_input())

for i in xrange(1, t + 1):
    st = raw_input()
    c = Counter(st)
    result = []
    # 0 2 4 5 6
    # For 0
    while c['Z'] > 0:
        result.append(0)
        c['Z'] -= 1
        c['E'] -= 1
        c['R'] -= 1
        c['O'] -= 1
    # For 2
    while c['W'] > 0:
        result.append(2)
        c['T'] -= 1
        c['W'] -= 1
        c['O'] -= 1
    # For 4
    while c['U'] > 0:
        result.append(4)
        c['F'] -= 1
        c['O'] -= 1
        c['U'] -= 1
        c['R'] -= 1
    # For 5
    while c['F'] > 0:
        result.append(5)
        c['F'] -= 1
        c['I'] -= 1
        c['V'] -= 1
        c['E'] -= 1
    # For 6
    while c['X'] > 0:
        result.append(6)
        c['S'] -= 1
        c['I'] -= 1
        c['X'] -= 1
    # For 7
    while c['S'] > 0:
        result.append(7)
        c['S'] -= 1
        c['E'] -= 2
        c['V'] -= 1
        c['N'] -= 1
    # For 8
    while c['G'] > 0:
        result.append(8)
        c['E'] -= 1
        c['I'] -= 1
        c['G'] -= 1
        c['H'] -= 1
        c['T'] -= 1
    # For 9
    while c['I'] > 0:
        result.append(9)
        c['N'] -= 2
        c['I'] -= 1
        c['E'] -= 1
    # For 1
    while c['O'] > 0:
        result.append(1)
        c['O'] -= 1
        c['N'] -= 1
        c['E'] -= 1
    # For 3
    while c['T'] > 0:
        result.append(3)
        c['T'] -= 1
        c['H'] -= 1
        c['R'] -= 1
        c['E'] -= 2

    result.sort()
    st = ''.join([str(j) for j in result])
    print("Case #{}: {}".format(i, st))
