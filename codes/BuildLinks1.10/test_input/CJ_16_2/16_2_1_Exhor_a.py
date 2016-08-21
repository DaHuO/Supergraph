digWords = ['ZREO','WTO','XIS','GHITE','UOFR','HTREE','NOE','VFIE','NNIE','VSEEN']
digNums = [0,2,6,8,4,3,1,5,9,7]
def containsDigit(s, digitword):
    while len(s) > 0:
        f = s.find(digitword[0])
        if f == -1:
            return '', False
        else:
            s = s[0:f]+s[f+1:]
            digitword = digitword[1:]
            if len(digitword) == 0:
                return s, True

def decnum(s,dtotry):
    guaranteeds = []
    changed = True;
    while changed:
        changed = False
        for digitwordid in dtotry:
            digitword = digWords[digitwordid]
            cando = False
            [swithoutd, cando] = containsDigit(s, digitword)
            if cando:
                changed = True
                guaranteeds = guaranteeds + [digNums[digitwordid]]
                s = swithoutd
                if len(s) == 0:
                    return s, guaranteeds
    return s, guaranteeds

def dnum(s):
    s2, guarantees = decnum(s,[0,1,2,3,4])
    if len(s2) == 0:
        return guarantees
    s3, g2 = decnum(s2,[5])
    if len(s3) == 0:
        return guarantees + g2
    s4, g3 = decnum(s3,[6])
    if len(s4) == 0:
        return guarantees + g2 + g3
    s5, g4 = decnum(s4,[7])
    if len(s5) == 0:
        return guarantees + g2 + g3 + g4
    s6, g5 = decnum(s5,[8])
    if len(s6) == 0:
        return guarantees + g2 + g3 + g4 + g5
    s7, g6 = decnum(s6,[9])
    if len(s7) == 0:
        return guarantees + g2 + g3 + g4 + g5 + g6
    else:
        print('fucccc')
    return []
    # s = s4
    # v = len([x for x in s if x == 'V'])
    # e = len([x for x in s if x == 'E'])
    #
    # tree = [(s,[])]
    # while len(tree) > 0:
    #     print( len(tree))
    #     ss, digs = tree[0]
    #     tree.pop(0)
    #     for d in range(7,10):
    #         [swithoutd, changed] = containsDigit(ss, digWords[d])
    #         if changed:
    #             if swithoutd == '':
    #                 return digs+[digNums[d]]+guarantees
    #             tree.append((swithoutd,digs+[digNums[d]]))

# import random
# for t in range(100):
#     S = ''
#     g = []
#     for i in range(400):
#         j = random.randint(0,9)
#         S = S + digWords[j]
#     dd = dnum(S)
#     print(t)

fi = open('A-large.in','r')
fo = open('out.txt','w')
T = int(fi.readline())
for ii in range(T):
    print('####### Case: ' + str(ii) + '#######')
    S = fi.readline()
    digs = dnum(S.replace('\n',''))
    nu = ''
    for d in sorted(digs):
        nu=nu+str(d)
    fo.write('Case #'+str(ii+1)+': '+nu+'\n')
fi.close()
fo.close()

