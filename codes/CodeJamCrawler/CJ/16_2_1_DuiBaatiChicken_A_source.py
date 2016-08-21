T = int(input())
ans = []
for t in range(0,T):
    s = input()
    temp = ''
    L = {}
    D = {}
    for i in range(0, len(s)):
        L[s[i]] = L.get(s[i],0) + 1
    while L.get('Z',0) > 0:
        D[0] = D.get(0,0) + 1
        L['Z'] -= 1
        L['E'] -= 1
        L['R'] -= 1
        L['O'] -= 1
    while L.get('W',0) > 0:
        D[2] = D.get(2,0) + 1
        L['T'] -= 1
        L['W'] -= 1
        L['O'] -= 1
    while L.get('X',0) > 0:
        D[6] = D.get(6,0) + 1
        L['S'] -= 1
        L['I'] -= 1
        L['X'] -= 1
    while L.get('G',0) > 0:
        D[8] = D.get(8,0) + 1
        L['E'] -= 1
        L['I'] -= 1
        L['G'] -= 1
        L['H'] -= 1
        L['T'] -= 1
    while L.get('H',0) > 0:
        D[3] = D.get(3,0) + 1
        L['T'] -= 1
        L['H'] -= 1
        L['R'] -= 1
        L['E'] -= 2
    while L.get('U',0) > 0:
        D[4] = D.get(4,0) + 1
        L['F'] -= 1
        L['O'] -= 1
        L['U'] -= 1
        L['R'] -= 1
    while L.get('O',0) > 0:
        D[1] = D.get(1,0) + 1
        L['O'] -= 1
        L['N'] -= 1
        L['E'] -= 1
    while L.get('F',0) > 0:
        D[5] = D.get(5,0) + 1
        L['F'] -= 1
        L['I'] -= 1
        L['V'] -= 1
        L['E'] -= 1
    while L.get('V',0) > 0:
        D[7] = D.get(7,0) + 1
        L['S'] -= 1
        L['E'] -= 2
        L['V'] -= 1
        L['N'] -= 1
    while L.get('N',0) > 0:
        D[9] = D.get(9,0) + 1
        L['N'] -= 2
        L['I'] -= 1
        L['E'] -= 1
    for i in range(0,10):
        for j in range(0,D.get(i,0)):
            temp+=str(i)
    ans.append('Case #'+str(t+1)+': '+temp)
for t in range(0,T):
    print(ans[t])
