from string import ascii_uppercase

def proc(rest):
    sz0 = rest['Z']
    rest['Z'] -= sz0
    rest['E'] -= sz0
    rest['R'] -= sz0
    rest['O'] -= sz0
    sz2 = rest['W']
    rest['T'] -= sz2
    rest['W'] -= sz2
    rest['O'] -= sz2
    sz4 = rest['U']
    rest['F'] -= sz4
    rest['O'] -= sz4
    rest['U'] -= sz4
    rest['R'] -= sz4
    sz3 = rest['R']
    rest['T'] -= sz3
    rest['H'] -= sz3
    rest['R'] -= sz3
    rest['E'] -= sz3 * 2
    sz6 = rest['X']
    rest['S'] -= sz6
    rest['I'] -= sz6
    rest['X'] -= sz6
    sz8 = rest['T']
    rest['E'] -= sz8
    rest['I'] -= sz8
    rest['G'] -= sz8
    rest['H'] -= sz8
    rest['T'] -= sz8
    sz1 = rest['O']
    rest['O'] -= sz1
    rest['N'] -= sz1
    rest['E'] -= sz1
    sz5 = rest['F']
    rest['F'] -= sz5
    rest['I'] -= sz5
    rest['V'] -= sz5
    rest['E'] -= sz5
    sz7 = rest['S']
    rest['E'] -= sz7*2
    rest['S'] -= sz7*2
    rest['V'] -= sz7*2
    rest['N'] -= sz7*2
    sz9 = rest['I']
    return [sz0,sz1,sz2,sz3,sz4,sz5,sz6,sz7,sz8,sz9]

times = int(input())
for t in range(times):
    inp = raw_input()
    rest={}
    #rest = {'Z':0,'W':0,'U':0,'R':0,'S':0,'T':0,'X':0,'O':0,'F':0}
    for c in ascii_uppercase:
        rest[c] = 0
    for c in inp:
        if c in rest:
            rest[c] += 1
        else:
            rest[c] = 1
    res = proc(rest)
    restr = ''
    for i in range(10):
        for j in range(res[i]):
            restr += str(i)
    print 'Case #'+str(t+1)+': '+restr
