T = int(input())
D = 1
alpha = ['Z','E','R','O','N','T','W','H','R','F','U','I','V','S','X','G']
while (D<=T):
    S = input()
    p = [0]*10
    d = {}
    for c in alpha:
        d[c] = 0
    for c in S:
        d[c] += 1
    #ZERO
    p[0] = d['Z']
    d['Z'] = 0
    if p[0]:
        d['E'] -= p[0]
        d['R'] -= p[0]
        d['O'] -= p[0]
    #TWO
    p[2] = d['W']
    d['W'] = 0
    if p[2]:
        d['T'] -= p[2]
        d['O'] -= p[2]
    #FOUR
    p[4] = d['U']
    d['U'] = 0
    if p[4]:
        d['F'] -= p[4]
        d['O'] -= p[4]
        d['R'] -= p[4]
    #THREE
    p[3] = d['R']
    d['R'] = 0
    if p[3]:
        d['T'] -= p[3]
        d['H'] -= p[3]
        d['E'] -= p[3]*2
    #FIVE
    p[5] = d['F']
    d['F'] = 0
    if p[5]:
        d['I'] -= p[5]
        d['V'] -= p[5]
        d['E'] -= p[5]
    #SIX
    p[6] = d['X']
    d['X'] = 0
    if p[6]:
        d['S'] -= p[6]
        d['I'] -= p[6]
    #SEVEN
    p[7] = d['V']
    d['V'] = 0
    if p[7]:
        d['S'] -= p[7]
        d['N'] -= p[7]
        d['E'] -= p[7]*2
    #ONE
    p[1] = d['O']
    d['O'] = 0
    if p[1]:
        d['N'] -= p[1]
        d['E'] -= p[1]
    #EIGHT
    p[8] = d['T']
    d['T'] = 0
    d['E'] -= p[8]
    #NINE
    p[9] = d['E']

    print("Case #" + str(D) + ": ",end="")
    for i in range(10):
        for _ in range(p[i]):
            print(i,end="")
    print()
    D += 1
