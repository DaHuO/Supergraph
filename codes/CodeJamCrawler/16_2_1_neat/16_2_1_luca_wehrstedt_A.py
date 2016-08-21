
def run():
    s = input().strip()
    di = dict((chr(x), 0) for x in range(ord('A'), ord("Z")+1))
    do = dict((x, 0) for x in range(10))
    for i in s:
        di[i] += 1

    if di['Z'] > 0:
        do[0] = di['Z']
        di['E'] -= di['Z']
        di['R'] -= di['Z']
        di['O'] -= di['Z']
        di['Z'] = 0
    if di['W'] > 0:
        do[2] = di['W']
        di['T'] -= di['W']
        di['O'] -= di['W']
        di['W'] = 0
    if di['X'] > 0:
        do[6] = di['X']
        di['S'] -= di['X']
        di['I'] -= di['X']
        di['X'] = 0
    if di['U'] > 0:
        do[4] = di['U']
        di['F'] -= di['U']
        di['O'] -= di['U']
        di['R'] -= di['U']
        di['U'] = 0
    if di['O'] > 0:
        do[1] = di['O']
        di['E'] -= di['O']
        di['N'] -= di['O']
        di['O'] = 0
    if di['R'] > 0:
        do[3] = di['R']
        di['T'] -= di['R']
        di['H'] -= di['R']
        di['E'] -= 2 * di['R']
        di['R'] = 0
    if di['H'] > 0:
        do[8] = di['H']
        di['E'] -= di['H']
        di['I'] -= di['H']
        di['G'] -= di['H']
        di['T'] -= di['H']
        di['H'] = 0
    if di['F'] > 0:
        do[5] = di['F']
        di['E'] -= di['F']
        di['I'] -= di['F']
        di['V'] -= di['F']
        di['F'] = 0
    if di['V'] > 0:
        do[7] = di['V']
        di['S'] -= di['V']
        di['N'] -= di['V']
        di['E'] -= 2 * di['V']
        di['V'] = 0
    if di['I'] > 0:
        do[9] = di['I']
        di['N'] -= 2 * di['I']
        di['E'] -= di['I']
        di['I'] = 0

    res = ""
    for i in range(10):
        res += do[i] * ("%d" % i)
    return res

t = int(input().strip())
for i in range(t):
    print("Case #%d: %s" % (i+1, run()))

