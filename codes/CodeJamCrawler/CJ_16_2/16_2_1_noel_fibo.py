for T in range(int(input())):
    st = input()
    dt = dict()
    for i in range(ord('A'),ord('Z')+1):
        dt[chr(i)] = 0
    for i in st:
        dt[i] += 1

    vs = ["" for i in range(10)]

    if dt['Z'] != 0:
        dt['E'] -= dt['Z']
        dt['R'] -= dt['Z']
        dt['O'] -= dt['Z']
        vs[0] = '0'*dt['Z']
        dt['Z'] =0

    if dt['W'] != 0:
        dt['O'] -= dt['W']
        dt['T'] -= dt['W']
        vs[2] = '2'*dt['W']
        dt['W'] = 0

    if dt['U'] != 0:
        dt['F'] -= dt['U']
        dt['O'] -= dt['U']
        dt['R'] -= dt['U']
        vs[4] = '4'*dt['U']
        dt['U'] = 0

    if dt['X'] != 0:
        dt['I'] -= dt['X']
        dt['S'] -= dt['X']
        vs[6] = '6'*dt['X']
        dt['X'] = 0


    if dt['G'] != 0:
        dt['E'] -= dt['G']
        dt['I'] -= dt['G']
        dt['H'] -= dt['G']
        dt['T'] -= dt['G']
        vs[8] = '8'*dt['G']
        dt['G'] = 0

    if dt['O'] != 0:
        dt['N'] -= dt['O']
        dt['E'] -= dt['O']
        vs[1] = '1'*dt['O']
        dt['O'] = 0


    if dt['R'] != 0:
        dt['T'] -= dt['R']
        dt['H'] -= dt['R']
        dt['E'] -= dt['R']
        dt['E'] -= dt['R']
        vs[3] = '3'*dt['R']
        dt['R'] = 0

    if dt['F'] != 0:
        dt['I'] -= dt['F']
        dt['V'] -= dt['F']
        dt['E'] -= dt['F']
        vs[5] = '5'*dt['F']
        dt['F'] = 0


    if dt['V'] != 0:
        dt['S'] -= dt['V']
        dt['E'] -= dt['V']
        dt['N'] -= dt['V']
        dt['E'] -= dt['V']
        vs[7] = '7'*dt['V']
        dt['V'] = 0


    if dt['N'] != 0:
        dt['I'] -= dt['N']//2
        dt['E'] -= dt['N']//2
        vs[9] = '9'*(dt['N']//2)
        dt['N'] = 0

    ans = ""
    for i in vs:
        ans+=i
    print("Case #{}: {}".format(T+1,ans))






